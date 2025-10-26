from flask import Flask, jsonify, request
from yahooquery import Screener
import pandas as pd

app = Flask(__name__)

@app.route('/gainers', methods=['GET'])
def get_gainers():
    """Get top gaining stocks"""
    try:
        s = Screener()
        data = s.get_screeners('day_gainers', count=25)
        
        if 'day_gainers' in data and 'quotes' in data['day_gainers']:
            stocks = data['day_gainers']['quotes']
            
            result = []
            for stock in stocks[:20]:
                result.append({
                    'symbol': stock.get('symbol'),
                    'name': stock.get('shortName') or stock.get('longName'),
                    'price': round(stock.get('regularMarketPrice', 0), 2),
                    'change': round(stock.get('regularMarketChange', 0), 2),
                    'change_percent': round(stock.get('regularMarketChangePercent', 0), 2),
                    'volume': stock.get('regularMarketVolume', 0),
                    'market_cap': stock.get('marketCap', 0),
                    'sector': stock.get('sector', 'Unknown')
                })
            
            return jsonify({'success': True, 'data': result})
        else:
            return jsonify({'success': False, 'error': 'No data available'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/losers', methods=['GET'])
def get_losers():
    """Get top losing stocks"""
    try:
        s = Screener()
        data = s.get_screeners('day_losers', count=25)
        
        if 'day_losers' in data and 'quotes' in data['day_losers']:
            stocks = data['day_losers']['quotes']
            
            result = []
            for stock in stocks[:20]:
                result.append({
                    'symbol': stock.get('symbol'),
                    'name': stock.get('shortName') or stock.get('longName'),
                    'price': round(stock.get('regularMarketPrice', 0), 2),
                    'change': round(stock.get('regularMarketChange', 0), 2),
                    'change_percent': round(stock.get('regularMarketChangePercent', 0), 2),
                    'volume': stock.get('regularMarketVolume', 0),
                    'market_cap': stock.get('marketCap', 0),
                    'sector': stock.get('sector', 'Unknown')
                })
            
            return jsonify({'success': True, 'data': result})
        else:
            return jsonify({'success': False, 'error': 'No data available'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/most-active', methods=['GET'])
def get_most_active():
    """Get most actively traded stocks"""
    try:
        s = Screener()
        data = s.get_screeners('most_actives', count=25)
        
        if 'most_actives' in data and 'quotes' in data['most_actives']:
            stocks = data['most_actives']['quotes']
            
            result = []
            for stock in stocks[:20]:
                result.append({
                    'symbol': stock.get('symbol'),
                    'name': stock.get('shortName') or stock.get('longName'),
                    'price': round(stock.get('regularMarketPrice', 0), 2),
                    'change': round(stock.get('regularMarketChange', 0), 2),
                    'change_percent': round(stock.get('regularMarketChangePercent', 0), 2),
                    'volume': stock.get('regularMarketVolume', 0),
                    'market_cap': stock.get('marketCap', 0),
                    'sector': stock.get('sector', 'Unknown')
                })
            
            return jsonify({'success': True, 'data': result})
        else:
            return jsonify({'success': False, 'error': 'No data available'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/trending', methods=['GET'])
def get_trending():
    """Get trending stocks"""
    try:
        s = Screener()
        data = s.get_screeners('aggressive_small_caps', count=25)
        
        if 'aggressive_small_caps' in data and 'quotes' in data['aggressive_small_caps']:
            stocks = data['aggressive_small_caps']['quotes']
            
            result = []
            for stock in stocks[:20]:
                result.append({
                    'symbol': stock.get('symbol'),
                    'name': stock.get('shortName') or stock.get('longName'),
                    'price': round(stock.get('regularMarketPrice', 0), 2),
                    'change': round(stock.get('regularMarketChange', 0), 2),
                    'change_percent': round(stock.get('regularMarketChangePercent', 0), 2),
                    'volume': stock.get('regularMarketVolume', 0),
                    'market_cap': stock.get('marketCap', 0),
                    'sector': stock.get('sector', 'Unknown')
                })
            
            return jsonify({'success': True, 'data': result})
        else:
            return jsonify({'success': False, 'error': 'No data available'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/52week-highs', methods=['GET'])
def get_52week_highs():
    """Get stocks at 52-week highs"""
    try:
        s = Screener()
        data = s.get_screeners('growth_technology_stocks', count=25)
        
        if 'growth_technology_stocks' in data and 'quotes' in data['growth_technology_stocks']:
            stocks = data['growth_technology_stocks']['quotes']
            
            result = []
            for stock in stocks[:20]:
                result.append({
                    'symbol': stock.get('symbol'),
                    'name': stock.get('shortName') or stock.get('longName'),
                    'price': round(stock.get('regularMarketPrice', 0), 2),
                    'change': round(stock.get('regularMarketChange', 0), 2),
                    'change_percent': round(stock.get('regularMarketChangePercent', 0), 2),
                    'volume': stock.get('regularMarketVolume', 0),
                    'market_cap': stock.get('marketCap', 0),
                    'sector': stock.get('sector', 'Unknown')
                })
            
            return jsonify({'success': True, 'data': result})
        else:
            return jsonify({'success': False, 'error': 'No data available'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/undervalued', methods=['GET'])
def get_undervalued():
    """Get undervalued stocks"""
    try:
        s = Screener()
        data = s.get_screeners('undervalued_large_caps', count=25)
        
        if 'undervalued_large_caps' in data and 'quotes' in data['undervalued_large_caps']:
            stocks = data['undervalued_large_caps']['quotes']
            
            result = []
            for stock in stocks[:20]:
                result.append({
                    'symbol': stock.get('symbol'),
                    'name': stock.get('shortName') or stock.get('longName'),
                    'price': round(stock.get('regularMarketPrice', 0), 2),
                    'change': round(stock.get('regularMarketChange', 0), 2),
                    'change_percent': round(stock.get('regularMarketChangePercent', 0), 2),
                    'volume': stock.get('regularMarketVolume', 0),
                    'market_cap': stock.get('marketCap', 0),
                    'sector': stock.get('sector', 'Unknown')
                })
            
            return jsonify({'success': True, 'data': result})
        else:
            return jsonify({'success': False, 'error': 'No data available'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/all-categories', methods=['GET'])
def get_all_categories():
    """Get all categories in one call"""
    try:
        s = Screener()
        
        categories = {
            'gainers': 'day_gainers',
            'losers': 'day_losers',
            'most_active': 'most_actives',
            'trending': 'aggressive_small_caps',
            'growth': 'growth_technology_stocks',
            'undervalued': 'undervalued_large_caps'
        }
        
        result = {}
        
        for key, screener_name in categories.items():
            try:
                data = s.get_screeners(screener_name, count=15)
                
                if screener_name in data and 'quotes' in data[screener_name]:
                    stocks = data[screener_name]['quotes']
                    
                    result[key] = []
                    for stock in stocks[:10]:
                        result[key].append({
                            'symbol': stock.get('symbol'),
                            'name': stock.get('shortName') or stock.get('longName'),
                            'price': round(stock.get('regularMarketPrice', 0), 2),
                            'change': round(stock.get('regularMarketChange', 0), 2),
                            'change_percent': round(stock.get('regularMarketChangePercent', 0), 2),
                            'volume': stock.get('regularMarketVolume', 0),
                            'market_cap': stock.get('marketCap', 0),
                            'sector': stock.get('sector', 'Unknown')
                        })
            except Exception as e:
                result[key] = []
                print(f"Error fetching {key}: {e}")
        
        return jsonify({
            'success': True,
            'date': pd.Timestamp.now().strftime('%Y-%m-%d'),
            'data': result
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'stock-api'})

@app.route('/', methods=['GET'])
def index():
    """API documentation"""
    return jsonify({
        'name': 'Stock Market API',
        'version': '1.0',
        'endpoints': {
            '/gainers': 'Get top gaining stocks',
            '/losers': 'Get top losing stocks',
            '/most-active': 'Get most actively traded stocks',
            '/trending': 'Get trending/volatile stocks',
            '/52week-highs': 'Get growth stocks near highs',
            '/undervalued': 'Get undervalued stocks',
            '/all-categories': 'Get all categories in one call (RECOMMENDED)',
            '/health': 'Health check'
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
