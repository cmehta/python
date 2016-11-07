'''
Make below fractal diagram
---0        ----0
-           -
--          --
-           ---
---1        ----1
            ---
            --
            -
            ----2
'''

def draw_ticks(tick_length, scale_value=''):
    line = '-'*tick_length
    if scale_value:
        line = line + ' ' + scale_value
    print(line)

def draw_interval(l):
    if l>0:
        draw_interval(l-1)
        draw_ticks(l)
        draw_interval(l-1)


def draw_ruler(major_length, inches):
    draw_ticks(major_length, '0')
    for j in range(1, 1+inches):
        draw_interval(major_length-1)
        draw_ticks(major_length, str(j))

draw_ruler(4,1)
