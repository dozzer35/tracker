from flask import Flask, request, send_file
import requests
from io import BytesIO

app = Flask(__name__)

# Telegram credentials
TELEGRAM_BOT_TOKEN = '7610905829:AAFwg61gCtcFvHdnRcBMDiz514iyUL84GRs'
TELEGRAM_CHAT_ID = '-4718696325'

@app.route('/open')
def track_open():
    email_id = request.args.get('email_id', 'unknown')

    # Send notification to Telegram
    message = f"📬 Email opened by: {email_id}"
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(telegram_url, data={
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    })

    # Serve a 1x1 transparent tracking pixel
    pixel = BytesIO(
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
        b'\xFF\xFF\xFF\x21\xF9\x04\x01\x00\x00\x00\x00\x2C\x00\x00\x00\x00'
        b'\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3B'
    )
    return send_file(pixel, mimetype='image/gif')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
