html_content = """<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>bw med amine | Official Links</title>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            /* Premium Dark Background */
            background: radial-gradient(circle at top, #1a1a1a 0%, #050505 100%);
            color: #ffffff;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 60px 20px;
        }

        /* Typography Focus (Since there is no image) */
        .header-container {
            text-align: center;
            margin-bottom: 50px;
        }

        h1.name-title {
            font-size: 36px;
            font-weight: 800;
            letter-spacing: 4px;
            text-transform: uppercase;
            background: linear-gradient(135deg, #ffffff 0%, #888888 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
            text-shadow: 0px 10px 20px rgba(255, 255, 255, 0.05);
        }
        
        .bio {
            font-size: 15px;
            color: #a0a0a0;
            font-weight: 300;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        /* Links Container */
        .links-container {
            display: flex;
            flex-direction: column;
            gap: 20px;
            width: 100%;
            max-width: 420px;
        }

        /* Glassmorphism Buttons */
        .link-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 18px 24px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 20px;
            text-decoration: none;
            color: #f1f1f1;
            font-size: 16px;
            font-weight: 500;
            letter-spacing: 1.5px;
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(12px);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }

        .link-btn i {
            position: absolute;
            left: 28px;
            font-size: 24px;
            transition: all 0.3s ease;
        }

        /* Hover Effects */
        .link-btn:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateY(-5px);
        }

        .link-btn.instagram:hover {
            border-color: #E1306C;
            box-shadow: 0 10px 25px rgba(225, 48, 108, 0.25);
        }
        .link-btn.instagram i { color: #E1306C; }

        .link-btn.tiktok:hover {
            border-color: #ff0050;
            box-shadow: 0 10px 25px rgba(255, 0, 80, 0.25);
        }
        .link-btn.tiktok i { color: #ff0050; }

        .link-btn.telegram:hover {
            border-color: #0088cc;
            box-shadow: 0 10px 25px rgba(0, 136, 204, 0.25);
        }
        .link-btn.telegram i { color: #0088cc; }

        .link-btn.discord:hover {
            border-color: #5865F2;
            box-shadow: 0 10px 25px rgba(88, 101, 242, 0.25);
        }
        .link-btn.discord i { color: #5865F2; }

        /* Footer */
        .footer {
            margin-top: 60px;
            font-size: 13px;
            color: #666;
            letter-spacing: 1px;
        }
    </style>
</head>
<body>

    <div class="header-container">
        <h1 class="name-title">bw med amine</h1>
        <div class="bio">Aesthetic Content Creator</div>
    </div>
    
    <div class="links-container">
        <!-- Instagram -->
        <a href="https://www.instagram.com/bw.med.amine?igsh=ZDdmdGg5bXl2ZjZz" target="_blank" class="link-btn instagram">
            <i class="fab fa-instagram"></i> Instagram
        </a>
        
        <!-- TikTok -->
        <a href="https://vt.tiktok.com/ZSQWB1Dut/" target="_blank" class="link-btn tiktok">
            <i class="fab fa-tiktok"></i> TikTok
        </a>
        
        <!-- Telegram -->
        <a href="https://t.me/Bw_medamine" target="_blank" class="link-btn telegram">
            <i class="fab fa-telegram"></i> Telegram
        </a>

        <!-- Discord -->
        <a href="https://discord.gg/Rf53XzN3" target="_blank" class="link-btn discord">
            <i class="fab fa-discord"></i> Discord
        </a>
    </div>
    
    <div class="footer">
        &copy; 2026 bw med amine. All rights reserved.
    </div>

</body>
</html>"""

with open("bw_med_amine_portfolio-v2.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("[file-tag: bw_med_amine_portfolio-v2.html]")