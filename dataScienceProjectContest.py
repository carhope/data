"""
교실 디스플레이 신호 유실(Flickering) 예측 모델 v2
- K-Fold 교차검증 도입 (소규모 샘플의 평가 불안정성 보완)
- 발표_시각(연속형) + 쉬는시간_직후_여부(파생 변수) 동시 사용 (Feature Engineering)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

# 한글 폰트 등록
_font_path = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
fm.fontManager.addfont(_font_path)
plt.rcParams["font.family"] = fm.FontProperties(fname=_font_path).get_name()
plt.rcParams["axes.unicode_minus"] = False

np.random.seed(42)

# -----------------------------
# 1. 가상 데이터셋 생성 (40개 샘플)
# -----------------------------
n = 40
연결_방식 = np.random.choice(["HDMI_유선", "AirPlay_무선", "동글_무선"], size=n, p=[0.4, 0.3, 0.3])
동시접속_기기수 = np.random.randint(10, 35, size=n)
배터리_잔량 = np.random.randint(5, 100, size=n)
케이블_동글_사용개월 = np.round(np.random.uniform(1, 40, size=n), 1)
발표_시각 = np.round(np.random.uniform(8.5, 16.5, size=n), 2)
발열_라벨 = np.random.choice([0, 1, 2], size=n, p=[0.5, 0.3, 0.2])
발열_이름 = {0: "정상", 1: "미온", 2: "고온경고"}

# [Feature Engineering] 도메인 지식 기반 파생변수: 쉬는시간/점심시간 직후 여부
# 실제 학교 시정표 기준: 쉬는시간(10~11시대, 12시대 일부) + 점심시간 직후(13~14시)
쉬는시간_직후_여부 = (
    ((발표_시각 >= 10.8) & (발표_시각 <= 11.2)) |
    ((발표_시각 >= 13.0) & (발표_시각 <= 14.0))
).astype(int)

무선_여부 = (연결_방식 != "HDMI_유선").astype(int)

# 종속변수 생성 확률식 (쉬는시간 직후 파생변수를 인과 요인으로 반영)
prob = (
    0.35 * (케이블_동글_사용개월 / 40)
    + 0.25 * (동시접속_기기수 / 35)
    + 0.15 * 무선_여부
    + 0.15 * (발열_라벨 / 2)
    + 0.10 * 쉬는시간_직후_여부
)
prob = np.clip(prob, 0, 1)
화면_깜빡임_발생 = np.random.binomial(1, prob)

df = pd.DataFrame({
    "연결_방식": 연결_방식,
    "동시접속_기기수": 동시접속_기기수,
    "배터리_잔량": 배터리_잔량,
    "케이블_동글_사용개월": 케이블_동글_사용개월,
    "발표_시각": 발표_시각,
    "쉬는시간_직후_여부": 쉬는시간_직후_여부,
    "기기_발열상태": [발열_이름[x] for x in 발열_라벨],
    "화면_깜빡임_발생": 화면_깜빡임_발생
})

print("=== 데이터셋 상위 5행 ===")
print(df.head())
print(f"\n총 샘플 수: {len(df)}개 | 깜빡임 발생 비율: {df['화면_깜빡임_발생'].mean()*100:.1f}%")

# -----------------------------
# 2. 전처리 (인코딩)
# -----------------------------
df_encoded = df.copy()
발열_map = {"정상": 0, "미온": 1, "고온경고": 2}
df_encoded["기기_발열상태"] = df_encoded["기기_발열상태"].map(발열_map)
df_encoded = pd.get_dummies(df_encoded, columns=["연결_방식"], prefix="연결")

X = df_encoded.drop(columns=["화면_깜빡임_발생"])
y = df_encoded["화면_깜빡임_발생"]

# -----------------------------
# 3. K-Fold 교차검증 (5-Fold) — 단일 분할의 불안정성 보완
# -----------------------------
model = DecisionTreeClassifier(max_depth=3, random_state=42)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=skf)

print(f"\n=== 5-Fold 교차검증 결과 ===")
print(f"Fold별 정확도: {np.round(cv_scores, 3)}")
print(f"평균 정확도: {cv_scores.mean()*100:.1f}% (표준편차: {cv_scores.std()*100:.1f}%p)")

# -----------------------------
# 4. 최종 모델 학습 (전체 데이터) + Fold별 변수중요도 평균
# -----------------------------
importances = []
for train_idx, _ in skf.split(X, y):
    m = DecisionTreeClassifier(max_depth=3, random_state=42)
    m.fit(X.iloc[train_idx], y.iloc[train_idx])
    importances.append(m.feature_importances_)

avg_importance = np.mean(importances, axis=0)
importance_df = pd.DataFrame({
    "변수": X.columns, "평균_중요도": avg_importance
}).sort_values("평균_중요도", ascending=False)

print("\n=== Fold 평균 변수 중요도 ===")
print(importance_df.to_string(index=False))

# -----------------------------
# 5. 시각화
# -----------------------------
plot_df = importance_df.sort_values("평균_중요도", ascending=True)
plt.figure(figsize=(8, 5))
plt.barh(plot_df["변수"], plot_df["평균_중요도"], color="#4C72B0")
plt.xlabel("평균 Feature Importance (5-Fold)")
plt.title("교실 TV 화면 깜빡임 원인 변수 중요도 (5-Fold 평균)")
plt.tight_layout()
plt.savefig("/home/claude/feature_importance_v2.png", dpi=150)
print("\n그래프 저장 완료: feature_importance_v2.png")