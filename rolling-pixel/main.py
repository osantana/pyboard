import pyb
import lcd160cr

lcd = lcd160cr.LCD160CR("X")
lcd.set_orient(lcd160cr.PORTRAIT)
lcd.erase()

accel = pyb.Accel()

lcd.set_text_color(1600, 0)
lcd.set_font(2)

red = lcd160cr.LCD160CR.rgb(255, 0, 0)
black = lcd160cr.LCD160CR.rgb(0, 0, 0)

x, y = int(lcd.w / 2), int(lcd.h / 2)

while True:
    dx, dy, dz = accel.filtered_xyz()

    dx = int(round(dx / 5, 0))
    dy = int(round(dy / 5, 0))

    x += dx
    y -= dy

    if x > lcd.w:
        x = lcd.w
    if x < 0:
        x = 0

    if y > lcd.h:
        y = lcd.h
    if y < 0:
        y = 0

    lcd.set_pixel(x, y, red)
    pyb.delay(100)
    lcd.set_pixel(x, y, black)
