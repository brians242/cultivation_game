# HELLO HUGE DISCLAIMER SECTION 

- 1) [download or copy ssh](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- 2) Run with python3 -m http.server 8000, then go to http://localhost/8000
- 3) click on cultivation_game_fixed. i might change this in the morning for more features idk we'll see
- 4) CHANGE LINE 480 TO YOUR ACTUAL CLAUDE API KEY SO IT ACTUALLY WORKS THE FALLBACKS ARE REALLY SCUFFED NGL cus i didnt put enough time in i spent so much effort
    - https://platform.claude.com/docs/en/api/admin/api_keys/retrieve (if you dont have one)
    - And if u dont wanna use claude gg i dont wanna figure out how u might do that sorry 😭😭😭😭😭
- it's kinda cooked ngl bro
- never done it outside of just asking claude if it can do the api calls to the .html file, so if it works it might not just be a user issue
   - Schrodinger ahh issue


# SOURCES AND CITATIONS
================================================

This document lists all sources and references used in the cultivation mystery game.

CODE SOURCES:
-------------

1. WebRTC Camera Access
   - Technology: MediaDevices.getUserMedia() API
   - Reference: MDN Web Docs - https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia
   - License: Public web standard (W3C)
   - Used for: Accessing user's webcam to detect colors

2. Canvas Color Detection
   - Technology: HTML5 Canvas API with getImageData()
   - Reference: MDN Web Docs - https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
   - License: Public web standard (W3C)
   - Used for: Extracting RGB color data from video feed

3. Color Detection Algorithm
   - Method: RGB averaging with dominant color detection
   - Based on: Standard color space algorithms (public domain)
   - Reference: Basic color theory (no specific source - mathematical averaging)
   - Used for: Determining user's dominant color from webcam

4. Anthropic Claude API
   - API: Claude Sonnet 4 via /v1/messages endpoint
   - Documentation: https://docs.anthropic.com
   - License: Anthropic API Terms of Service
   - Used for: Generating dynamic cultivation story content and choices

CONTENT GENERATION (As per Claude):
-------------------

1. Cultivation Story Content
   - Source: Generated dynamically by Claude API
   - Method: AI-generated original content per session
   - Theme: Cultivation/Xianxia genre conventions (public tropes)
   - License: Generated content (original)
   - Fallbacks: Generated through scraping and other program data cleaning into the json file

2. Cultivation Paths & Elements
   - Inspiration: Traditional Chinese Five Elements (Wu Xing) - public domain
   - Reference: General cultivation novel tropes (genre conventions)
   - License: Public domain concepts
   - Names: Original creations (Crimson Flame Sect, Azure Ocean Monastery, etc.)

3. Mystery Theme
   - Concept: "The Emerald Truth" 
   - Source: Original creation
   - License: Original content

TECHNICAL LIBRARIES:
--------------------

None required - Pure vanilla HTML/CSS/JavaScript implementation
- No external dependencies
- No third-party libraries
- Uses only native browser APIs

CULTIVATION GENRE REFERENCES:
-----------------------------

General cultivation/xianxia tropes used (public genre conventions):
- Cultivation realms and progression
- Elemental affinities
- Sect/clan structures
- Qi/spiritual energy concepts
- Enlightenment and breakthroughs

These are genre conventions similar to "space marines" in sci-fi or "dragons" in fantasy - 
publicly available story elements not owned by any specific work.

EDUCATIONAL FAIR USE NOTES:
---------------------------

This project was created for educational purposes to demonstrate:
- WebRTC camera integration
- Dynamic content generation with AI APIs
- Game state management in JavaScript
- Responsive web design with CSS
- API integration patterns

No copyrighted materials were scraped or reproduced.
All content is either:
1. Generated dynamically via API
2. Original creation
3. Public domain concepts
4. Standard web technologies

LICENSE SUMMARY:
----------------

- Code: Original (you may use as you wish)
- Design: Original
- Content: Dynamically generated (Anthropic API usage terms apply)
- Technologies: Public web standards

ATTRIBUTION:
------------

If you use this code, please credit:
- WebRTC camera code: W3C Web Standards
- Claude API: Anthropic
- Original implementation: This project

Last Updated: February 2, 2026
