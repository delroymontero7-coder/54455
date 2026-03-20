def run_scan():
    return {
        "status": "ok",
        "message": "Scan completed successfully"
    }

def download_symbol(symbol="BTC"):
    return {
        "symbol": symbol,
        "data": [],
        "status": "downloaded"
    }
