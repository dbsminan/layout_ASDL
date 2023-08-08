from function import *

#grating coupler 위치, 방향 변수
x_position = 0
y_position = 0
rotation_angle = 90
#waveguide 변수
l = 40
r = 30
w = 0.5
w_c = 20.5
a = 90
#빈 box 변수
l_box = 80
w_box = 50

#component 생성
d = gf.Component()

#각각의 필요한 grating coupler, waveguide, mmi 생성
GC = create_grating_coupler()
GC2 = create_grating_coupler()
WG_st1 = create_waveguide_straight(l,w)
WG_b1 = create_waveguide_bend(r,w,a)
WG_st2 = create_waveguide_straight(l,w)
MMI_1 = create_mmi()

WG_2_b1 = create_waveguide_bend(r,w,a)
WG_3_b1 = create_waveguide_bend(r,w,a)
WG_2_b2 = create_waveguide_bend(r,w,a)
WG_3_b2 = create_waveguide_bend(r,w,a)

Box_2 = create_waveguide_straight(l_box,w_box)
Box_3 = create_waveguide_straight(l_box,w_box)

WG_2_b3 = create_waveguide_bend(r,w,a)
WG_3_b3 = create_waveguide_bend(r,w,a)

WG_2_b4 = create_waveguide_bend(r,w,a)
WG_3_b4 = create_waveguide_bend(r,w,a)

MMI_2 = create_mmi()

WG_b2 = create_waveguide_bend(r,w,a)
WG_st3 = create_waveguide_straight(l,w)

WG_st1_c = create_waveguide_straight(l,w_c)
WG_b1_c = create_waveguide_bend(r,w_c,a)
WG_st2_c = create_waveguide_straight(l,w_c)


WG_2_b1_c = create_waveguide_bend(r,w_c,a)
WG_3_b1_c = create_waveguide_bend(r,w_c,a)
WG_2_b2_c = create_waveguide_bend(r,w_c,a)
WG_3_b2_c = create_waveguide_bend(r,w_c,a)

WG_2_b3_c = create_waveguide_bend(r,w_c,a)
WG_3_b3_c = create_waveguide_bend(r,w_c,a)
WG_2_b4_c = create_waveguide_bend(r,w_c,a)
WG_3_b4_c = create_waveguide_bend(r,w_c,a)

WG_b2_c = create_waveguide_bend(r,w_c,a)
WG_st3_c = create_waveguide_straight(l,w_c)


#생성한 요소들을 component에 추가
gc = d << GC
gc2 = d << GC2
wg_st1 = d << WG_st1
wg_b1 = d << WG_b1
wg_st2 = d << WG_st2
mmi_1 = d << MMI_1

wg_2_b1 = d << WG_2_b1
wg_3_b1 = d << WG_3_b1
wg_2_b2 = d << WG_2_b2
wg_3_b2 = d << WG_3_b2

box_2 = d << Box_2
box_3 = d << Box_3

wg_2_b3 = d << WG_2_b3
wg_3_b3 = d << WG_3_b3

wg_2_b4 = d << WG_2_b4
wg_3_b4 = d << WG_3_b4

mmi_2 = d << MMI_2

wg_b2 = d << WG_b2
wg_st3 = d << WG_st3

wg_st1_c = d << WG_st1_c
wg_b1_c = d << WG_b1_c
wg_st2_c = d << WG_st2_c


wg_2_b1_c = d << WG_2_b1_c
wg_3_b1_c = d << WG_3_b1_c
wg_2_b2_c = d << WG_2_b2_c
wg_3_b2_c = d << WG_3_b2_c

wg_2_b3_c = d << WG_2_b3_c
wg_3_b3_c = d << WG_3_b3_c
wg_2_b4_c = d << WG_2_b4_c
wg_3_b4_c = d << WG_3_b4_c

wg_b2_c = d << WG_b2_c
wg_st3_c = d << WG_st3_c
#grating coupler 초기 위치, 방향 설정
gc = move_rotate(gc, x_position, y_position, rotation_angle)

#각 요소에 port 생성
d.add_port('gc', port=gc['o1'])
d.add_port('gc2', port=gc2['o1'])

wg1_ports = add_ports(wg_st1)
wg2_ports = add_ports(wg_b1)
wg_st2_ports = add_ports(wg_st2)

mmi1_ports = add_ports(mmi_1)

wg_2_b1_ports = add_ports(wg_2_b1)
wg_3_b1_ports = add_ports(wg_3_b1)

wg_2_b2_ports = add_ports(wg_2_b2)
wg_3_b2_ports = add_ports(wg_3_b2)

box_2_ports = add_ports(box_2)
box_3_ports = add_ports(box_3)

wg_2_b3_ports = add_ports(wg_2_b3)
wg_3_b3_ports = add_ports(wg_3_b3)

wg_2_b4_ports = add_ports(wg_2_b4)
wg_3_b4_ports = add_ports(wg_3_b4)

mmi2_ports = add_ports(mmi_2)

wg_b2_ports = add_ports(wg_b2)
wg_st3_ports = add_ports(wg_st3)

# ----------------------------------------
wg1_c_ports = add_ports(wg_st1_c)
wg2_c_ports = add_ports(wg_b1_c)
wg_st2_c_ports = add_ports(wg_st2_c)


wg_2_b1_c_ports = add_ports(wg_2_b1_c)
wg_3_b1_c_ports = add_ports(wg_3_b1_c)
wg_2_b2_c_ports = add_ports(wg_2_b2_c)
wg_3_b2_c_ports = add_ports(wg_3_b2_c)

wg_2_b3_c_ports = add_ports(wg_2_b3_c)
wg_3_b3_c_ports = add_ports(wg_3_b3_c)
wg_2_b4_c_ports = add_ports(wg_2_b4_c)
wg_3_b4_c_ports = add_ports(wg_3_b4_c)

wg_b2_c_ports = add_ports(wg_b2_c)
wg_st3_c_ports = add_ports(wg_st3_c)

#connect
wg_st1.connect('o1', destination=gc['o1'])
wg_b1.connect('o1', destination=wg_st1['o2'])
wg_st2.connect('o1', destination=wg_b1['o2'])
mmi_1.connect('o1', destination=wg_st2['o2'])

wg_2_b1.connect('o1', destination=mmi_1['o2'])
wg_3_b1.connect('o2', destination=mmi_1['o3'])
wg_2_b2.connect('o2', destination=wg_2_b1['o2'])
wg_3_b2.connect('o1', destination=wg_3_b1['o1'])

box_2.connect('o1', destination=wg_2_b2['o1'])
box_3.connect('o1', destination=wg_3_b2['o2'])

wg_2_b3.connect('o2', destination=box_2['o2'])
wg_3_b3.connect('o1', destination=box_3['o2'])

wg_2_b4.connect('o1', destination=wg_2_b3['o1'])
wg_3_b4.connect('o2', destination=wg_3_b3['o2'])

mmi_2.connect('o3', destination=wg_2_b4['o2'])
mmi_2.connect('o2', destination=wg_3_b4['o1'])

wg_b2.connect('o2', destination=mmi_2['o1'])
wg_st3.connect('o1', destination=wg_b2['o1'])

gc2.connect('o1', destination=wg_st3['o2'])
# ------------------------------------------------------
wg_st1_c.connect('o1', destination=gc['o1'])
wg_b1_c.connect('o1', destination=wg_st1['o2'])
wg_st2_c.connect('o1', destination=wg_b1['o2'])


wg_2_b1_c.connect('o1', destination=mmi_1['o2'])
wg_3_b1_c.connect('o2', destination=mmi_1['o3'])
wg_2_b2_c.connect('o2', destination=wg_2_b1_c['o2'])
wg_3_b2_c.connect('o1', destination=wg_3_b1_c['o1'])

wg_2_b3_c.connect('o2', destination=box_2['o2'])
wg_3_b3_c.connect('o1', destination=box_3['o2'])
wg_2_b4_c.connect('o1', destination=wg_2_b3_c['o1'])
wg_3_b4_c.connect('o2', destination=wg_3_b3_c['o2'])

wg_b2_c.connect('o2', destination=mmi_2['o1'])
wg_st3_c.connect('o1', destination=wg_b2_c['o1'])