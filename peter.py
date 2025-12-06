import yfinance as yf
import pandas as pd

# 피터 린치의 조언: "모니터 앞에서 너무 많은 시간을 보내지 마세요."
# 하지만 이 코드는 당신의 시간을 아껴줄 겁니다.

def peter_lynch_screener(tickers):
    opportunities = []

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            # 1. 기본 데이터 가져오기
            pe_ratio = info.get('trailingPE')
            forward_pe = info.get('forwardPE')
            earnings_growth = info.get('earningsQuarterlyGrowth', 0)  # 분기 이익 성장률
            peg_ratio = info.get('pegRatio')
            debt_to_equity = info.get('debtToEquity', 1000) # 부채비율
            dividend_yield = info.get('dividendYield', 0) # 배당수익률

            # 데이터가 없으면 건너뜁니다. (이해할 수 없는 기업은 패스!)
            if pe_ratio is None or earnings_growth is None:
                continue

            # --- 피터 린치의 체크리스트 ---

            # A. PEG 비율 체크 (가장 중요!)
            # 배당이 있다면 성장률에 배당수익률을 더해서 계산 (PEGY)
            growth_rate = (earnings_growth * 100) # 퍼센트로 변환
            adjusted_growth = growth_rate + (dividend_yield * 100 if dividend_yield else 0)

            if adjusted_growth > 0:
                lynch_metric = pe_ratio / adjusted_growth
            else:
                lynch_metric = 100 # 성장이 없으면 탈락

            # 0.5 이하면 '강력 매수', 1.0 이하면 '적정'
            if lynch_metric > 1.5:
                continue 

            # B. 재무 건전성 (부채)
            # 빚이 너무 많으면 턴어라운드주가 아니라 그냥 망하는 주식입니다.
            # 부채비율 50% 이하 선호 (금융주는 예외지만 여기선 보수적으로)
            if debt_to_equity > 80: 
                continue

            # C. 분류 (Categorization) - 숫자로 대략적 추정
            category = "알 수 없음"
            if growth_rate < 10:
                category = "저성장주 (Slow Grower)"
            elif 10 <= growth_rate < 20:
                category = "대형 우량주 (Stalwart)"
            elif 20 <= growth_rate < 50:
                category = "고성장주 (Fast Grower)" # 제가 제일 좋아합니다!
            elif growth_rate >= 50:
                category = "초고속 성장주 (주의 요망!)"

            # 리스트에 추가
            opportunities.append({
                'Ticker': ticker,
                'Name': info.get('shortName'),
                'Category': category,
                'Price': info.get('currentPrice'),
                'PE': round(pe_ratio, 2),
                'Growth(%)': round(growth_rate, 2),
                'PEG/PEGY': round(lynch_metric, 2),
                'Debt/Equity': debt_to_equity
            })

        except Exception as e:
            # "문제가 생기면 그냥 덮으세요. 주식은 많습니다."
            print(f"Error analyzing {ticker}: {e}")
            continue

    return pd.DataFrame(opportunities)

# 사용 예시: 관심 있는 티커들을 리스트에 넣으세요.
# (실제로는 S&P500 전체 티커 등을 넣어서 돌립니다)
my_watchlist = ['AAPL', 'KO', 'TSLA', 'GOOGL', 'MCD', 'INTC', 'F']
df = peter_lynch_screener(my_watchlist)

# 결과 출력 (PEG가 낮은 순서대로 정렬)
if not df.empty:
    print(df.sort_values(by='PEG/PEGY'))
else:
    print("살만한 주식이 하나도 안 보이는군요! 현금을 쥐고 기다리세요.")
