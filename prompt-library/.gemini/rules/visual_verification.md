# Visual Verification Protocol (The Ghost)

## 0. The Philosophy
> "Code compiles, tests pass, but the button is off-screen. To the user, it is broken."
> We trust **Pixels** over **Code**.

## 1. The Ghost Protocol (E2E)
* **Tool of Choice:** Playwright (Preferred) or Puppeteer.
* **No Headless Blindness:** Tests must be designed as if a human is watching.
    * **Visible Wait:** Do not use hard `sleep()`. Wait for element visibility (`toBeVisible()`).
    * **User Action:** Click, Type, Scroll like a human (add slight delays/jitter if needed for realism).

## 2. Visual Regression Standards
* **Snapshot Testing:** Compare current UI against "Golden Master" screenshots.
* **Responsive Check:** Always verify critical flows on **Mobile (375px)** and **Desktop (1920px)**.
* **Layout Stability:** Check for Cumulative Layout Shift (CLS). Elements should not jump around.

## 3. The "Happy Path" Visualization
* Before verifying edge cases, record a video/trace of the "Happy Path" (The ideal user journey).
* If the Happy Path looks wrong, stop testing and fix the UI.