from function import *

#grating coupler 위치, 방향 변수
x_position = 0
y_position = 0
rotation_angle = 90
#waveguide 변수
l = 20
r = 10
w = 0.5
a = 90

#component 생성
c= gf.Component()

#layer (10/0),(11/0),(11/1),(11/9),(11/11)
#코드 차이로 polygon은 따로 생성
#layer 11,9의 폴리곤
poly1 = c.add_polygon([(-101.7,-165.55,-125.55,-98.3),(-110.4,-10.4,-10.4,-110.4)],layer=(11,9))
poly1 = c.add_polygon([(98.3,34.45,74.45,101.7),(-110.4,-10.4,-10.4,-110.4)],layer=(11,9))
poly1 = c.add_polygon([(-165.55,-101.7,-98.3,-125.55),(-1750.4,-1650.4,-1650.4,-1750.4)],layer=(11,9))
poly1 = c.add_polygon([(34.45,98.275,101.675,74.45),(-1750.4,-1650.4,-1650.4,-1750.4)],layer=(11,9))
poly1 = c.add_polygon([(-92.8,-65.55,-25.55,-89.4),(-110.4,-10.4,-10.4,-110.4)],layer=(11,9))
poly1 = c.add_polygon([(107.2,134.45,174.45,110.6),(-110.4,-10.4,-10.4,-110.4)],layer=(11,9))
poly1 = c.add_polygon([(-65.55,-92.8,-89.4,-25.55),(-1750.4,-1650.4,-1650.4,-1750.4)],layer=(11,9))
poly1 = c.add_polygon([(134.45,107.2,110.6,174.45),(-1750.4,-1650.4,-1650.4,-1750.4)],layer=(11,9))

#layer 11,1의 폴리곤
poly2 = c.add_polygon([(-151.7,-225.55,-165.55,-101.7),(-110.4,-10.4,-10.4,-110.4)],layer=(11,1))
poly2 = c.add_polygon([(-89.4,-25.55,34.45,-39.4),(-110.4,-10.4,-10.4,-110.4)],layer=(11,1))
poly2 = c.add_polygon([(48.3,-25.55,34.45,98.3),(-110.4,-10.4,-10.4,-110.4)],layer=(11,1))
poly2 = c.add_polygon([(110.6,174.45,234.45,160.6),(-110.4,-10.4,-10.4,-110.4)],layer=(11,1))
poly2 = c.add_polygon([(-225.55,-151.7,-101.7,-165.55),(-1750.4,-1650.4,-1650.4,-1750.4)],layer=(11,1))
poly2 = c.add_polygon([(-25.55,-89.4,-39.4,34.45),(-1750.4,-1650.4,-1650.4,-1750.4)],layer=(11,1))
poly2 = c.add_polygon([(-25.55,48.3,98.3,34.45),(-1750.4,-1650.4,-1650.4,-1750.4)],layer=(11,1))
poly2 = c.add_polygon([(174.45,110.6,160.6,234.45),(-1750.4,-1650.4,-1650.4,-1750.4)],layer=(11,1))

#layer 11,11의 box array
BOX_ARRAY1 = create_rectangle(0.6,0.6,11,11)
BOX_ARRAY1 = create_array(BOX_ARRAY1,1.8,1.8,30,40)
BOX_ARRAY1 = create_array(BOX_ARRAY1,100,1820,5,2)
box_array1 = c << BOX_ARRAY1
box_array1 = move_rotate(box_array1, -221.95, -1825.8, 0)

#layer 11,9의 box array
BOX_ARRAY2 = create_rectangle(3.4,1540,11,9)
BOX_ARRAY2 = create_array(BOX_ARRAY2,8.9,0,2,1)
BOX_ARRAY2 = create_array(BOX_ARRAY2,200,0,2,1)
box_array2 = c << BOX_ARRAY2
box_array2 = move_rotate(box_array2, -101.7, -1650.4, 0)

BOX_ARRAY3 = create_rectangle(5.5,1540,11,9)
BOX_ARRAY3 = create_array(BOX_ARRAY3,200,0,2,1)
box_array3 = c << BOX_ARRAY3
box_array3 = move_rotate(box_array3, -98.3, -1650.4, 0)

#layer 11,1의 box array
BOX_ARRAY4 = create_rectangle(60,80,11,1)
BOX_ARRAY4 = create_array(BOX_ARRAY4,100,0,5,1)
BOX_ARRAY4 = create_array(BOX_ARRAY4,0,1820,1,2)
box_array4 = c << BOX_ARRAY4
box_array4 = move_rotate(box_array4, -225.55, -1830.4, 0)

BOX_ARRAY5 = create_rectangle(1.94,35.6,11,1)
BOX_ARRAY5 = create_array(BOX_ARRAY5,41.94,0,2,1)
BOX_ARRAY5 = create_array(BOX_ARRAY5,100,0,4,1)
box_array5 = c << BOX_ARRAY5
box_array5 = move_rotate(box_array5, -167.49, 11.8, 0)

BOX_ARRAY6 = create_rectangle(0.35,0.35,11,1)
BOX_ARRAY6 = create_array(BOX_ARRAY6,0.6,0.6,3,58)
BOX_ARRAY6 = create_array(BOX_ARRAY6,41.8,0,2,1)
BOX_ARRAY6 = create_array(BOX_ARRAY6,100,0,4,1)
box_array6 = c << BOX_ARRAY6
box_array6 = move_rotate(box_array6, -167.225, 12.325, 0)

BOX_ARRAY7 = create_rectangle(50,1540,11,1)
BOX_ARRAY7 = create_array(BOX_ARRAY7,62.3,0,2,1)
BOX_ARRAY7 = create_array(BOX_ARRAY7,200,0,2,1)
box_array7 = c << BOX_ARRAY7
box_array7 = move_rotate(box_array7, -151.7, -1650.4, 0)

BOX_ARRAY8 = create_rectangle(60,44,11,1)
BOX_ARRAY8 = create_array(BOX_ARRAY8,0,1696,1,2)
box_array8 = c << BOX_ARRAY8
box_array8 = move_rotate(box_array8, -25.55, -1750.4, 0)

BOX_ARRAY9 = create_rectangle(5.5,1540,11,1)
BOX_ARRAY9 = create_array(BOX_ARRAY9,200,0,2,1)
box_array9 = c << BOX_ARRAY9
box_array9 = move_rotate(box_array9, -98.3, -1650.4, 0)

BOX_ARRAY10 = create_rectangle(5.5,3,11,1)
BOX_ARRAY10 = create_array(BOX_ARRAY10,0,3,1,500)
BOX_ARRAY10 = create_array(BOX_ARRAY10,8.9,0,2,1)
BOX_ARRAY10 = create_array(BOX_ARRAY10,200,0,2,1)
box_array10 = c << BOX_ARRAY10
box_array10 = move_rotate(box_array10, -107.2, -1630.4, 0)

BOX_ARRAY11 = create_rectangle(0.35,0.35,11,1)
BOX_ARRAY11 = create_array(BOX_ARRAY11,0.6,0.6,3,2500)
BOX_ARRAY11 = create_array(BOX_ARRAY11,5.2,0,2,1)
BOX_ARRAY11 = create_array(BOX_ARRAY11,200,0,2,1)
box_array11 = c << BOX_ARRAY11
box_array11 = move_rotate(box_array11, -103.375, -1630.285, 0)

#layer 11,1의 taper
taper1 = c << create_taper(100,60,5.5,11,1)
taper1 = move_rotate(taper1, -95.55, -10.4, -90)

taper2 = c << create_taper(100,60,5.5,11,1)
taper2 = move_rotate(taper2, 104.45, -10.4, -90)

taper3 = c << create_taper(100,60,5.5,11,1)
taper3 = move_rotate(taper3, -95.55, -1750.4, 90)

taper4 = c << create_taper(100,60,5.5,11,1)
taper4 = move_rotate(taper4, 104.45, -1750.4, 90)

#layer 10,10의 circle array
Circle = create_circle(0.155, 14, 11)
Circle1_array = create_array(Circle, 0.6, 0.6, 3, 58)
Circle1_array = create_array(Circle1_array, 41.8, 0, 2, 1)
Circle1_array = create_array(Circle1_array, 100, 0, 4, 1)
circle1_array = c << Circle1_array
circle1_array = move_rotate(circle1_array, -167.05, 12.5, 0)

Circle2_array = create_array(Circle, 0.6, 0.6, 3, 2500)
Circle2_array = create_array(Circle2_array, 5.2, 0, 2, 1)
Circle2_array = create_array(Circle2_array, 194.8, 0, 2, 1)
circle2_array = c << Circle2_array
circle2_array = move_rotate(circle2_array, -103.2, -1630.1, 0)

#layer (37/4),(37/5)
#taper 생성
u_taper1 = c << create_taper(10,0.5,2,37,4)
u_taper2 = c << create_taper(10,0.5,2,37,4)
d_taper1 = c << create_taper(10,0.5,2,37,4)
d_taper2 = c << create_taper(10,0.5,2,37,4)

#빈박스(수정해야함)
box1 = c << create_waveguide_straight(1503.8, w,37,4)
box2 = c << create_waveguide_straight(1503.8, w,37,4)
box1_p = add_ports(box1)
box2_p = add_ports(box2)

# ---오른쪽 taper---
wg_rst1 = c << create_waveguide_straight(0.2,w,37,4)
wg_rst2 = c << create_waveguide_straight(26,w,37,4)
wg_rb1 = c << create_waveguide_bend(r,w,a,37,4)
wg_rst3 = c << create_waveguide_straight(78.35,w,37,4)
wg_rb2 = c << create_waveguide_bend(r,w,a,37,4)
wg_rst4 = c << create_waveguide_straight(0.2,w,37,4)
wg_rst5 = c << create_waveguide_straight(1,w,37,4)
wg_rst6 = c << create_waveguide_straight(0.2,w,37,4)
#---왼쪽 taper---
wg_lst1 = c << create_waveguide_straight(0.2,w,37,4)
wg_lst2 = c << create_waveguide_straight(26,w,37,4)
wg_lb1 = c << create_waveguide_bend(r,w,a,37,4)
wg_lst3 = c << create_waveguide_straight(78.35,w,37,4)
wg_lb2 = c << create_waveguide_bend(r,w,a,37,4)
wg_lst4 = c << create_waveguide_straight(0.2,w,37,4)
wg_lst5 = c << create_waveguide_straight(1,w,37,4)
wg_lst6 = c << create_waveguide_straight(0.2,w,37,4)
#mmi
mmi1 = c << create_mmi(55,12)
mmi1 = move_rotate(mmi1,0,0, -90)

mmi1_c = c << gf.components.mmi1x2(length_mmi=55, width_mmi=20, width_taper=17,gap_mmi=-20.3, width=4.45)
mmi1_c = move_rotate(mmi1_c,0,0, -90)
#mmi 위쪽
wg_st1 = c << create_waveguide_straight(0.2,w,37,4)
wg_st2 = c << create_waveguide_straight(1,w,37,4)
wg_st3 = c << create_waveguide_straight(0.2,w,37,4)
wg_b1 = c << create_waveguide_bend(30,w,16,37,4)
wg_b2 = c << create_waveguide_bend(30,w,16,37,4)
wg_st4 = c << create_waveguide_straight(50,w,37,4)
wg_b3 = c << create_waveguide_bend(r,w,a,37,4)
wg_st5 = c << create_waveguide_straight(175,w,37,4)
wg_b4 = c << create_waveguide_bend(r,w,a,37,4)
wg_st6 = c << create_waveguide_straight(940,w,37,4)
wg_b5 = c << create_waveguide_bend(r,w,a,37,4)
wg_st7 = c << create_waveguide_straight(10,w,37,4)
wg_st8 = c << create_waveguide_straight(0.2,w,37,4)
wg_st9 = c << create_waveguide_straight(0.2,w,37,4)

#rectangle 4x1 array
rec = create_rectangle(44.08,35.6,37,4)
rec_arr = c << create_array(rec,100,1,4,1)
rec_arr = move_rotate(rec_arr,-167.59,11.8,0)

rec_c = create_rectangle(45.08,36.6,37,5)
rec_c_arr = c << create_array(rec_c,100,1,4,1)
rec_c_arr = move_rotate(rec_c_arr,-168.09,11.3,0)

#위쪽 waveguide
u_st1 = c << create_waveguide_straight(0.2,w,37,4)
u_st1 = move_rotate(u_st1,212, -837,0)
u_st2 = c << create_waveguide_straight(0.2,w,37,4)
u_b1 = c << create_waveguide_bend(r,w,a,37,4)
u_st3 = c << create_waveguide_straight(914,w,37,4)
u_b2 = c << create_waveguide_bend(r,w,a,37,4)
u_st4 = c << create_waveguide_straight(380,w,37,4)
u_b3 = c << create_waveguide_bend(r,w,a,37,4)
u_st5 = c << create_waveguide_straight(914,w,37,4)
u_b4 = c << create_waveguide_bend(r,w,a,37,4)
u_st6 = c << create_waveguide_straight(0.2,w,37,4)
u_st7 = c << create_waveguide_straight(0.2,w,37,4)

#아래쪽 waveguide
mmi2 = c << create_mmi(55,12)
mmi2 = move_rotate(mmi2,0,-1789, 90)
#mmi 왼쪽
d_lst1 = c << create_waveguide_straight(0.2,w,37,4)
d_lst2 = c << create_waveguide_straight(1,w,37,4)
d_lst3 = c << create_waveguide_straight(0.2,w,37,4)
d_lst4 = c << create_waveguide_straight(10,w,37,4)
d_lb1 = c << create_waveguide_bend(r,w,a,37,4)
d_lst5 = c << create_waveguide_straight(78.35,w,37,4)
d_lb2 = c << create_waveguide_bend(r,w,a,37,4)
d_lb3 = c << create_waveguide_bend(r,w,a,37,4)
d_lst6 = c << create_waveguide_straight(5,w,37,4)
d_lb4 = c << create_waveguide_bend(r,w,a,37,4)
d_lb5 = c << create_waveguide_bend(r,w,a,37,4)
d_lst7 = c << create_waveguide_straight(5,w,37,4)
d_lb6 = c << create_waveguide_bend(r,w,a,37,4)
d_lst8 = c << create_waveguide_straight(16,w,37,4)
d_lst9 = c << create_waveguide_straight(0.2,w,37,4)

#mmi 오른쪽
d_rst1 = c << create_waveguide_straight(0.2,w,37,4)
d_rst2 = c << create_waveguide_straight(1,w,37,4)
d_rst3 = c << create_waveguide_straight(0.2,w,37,4)
d_rst4 = c << create_waveguide_straight(10,w,37,4)
d_rb1 = c << create_waveguide_bend(r,w,a,37,4)
d_rst5 = c << create_waveguide_straight(78.35,w,37,4)
d_rb2 = c << create_waveguide_bend(r,w,a,37,4)
d_rb3 = c << create_waveguide_bend(r,w,a,37,4)
d_rst6 = c << create_waveguide_straight(25,w,37,4)
d_rb4 = c << create_waveguide_bend(r,w,a,37,4)
d_rb5 = c << create_waveguide_bend(r,w,a,37,4)
d_rst7 = c << create_waveguide_straight(25,w,37,4)
d_rb6 = c << create_waveguide_bend(r,w,a,37,4)
d_rst8 = c << create_waveguide_straight(16,w,37,4)
d_rst9 = c << create_waveguide_straight(0.2,w,37,4)

#mmi 아래쪽
d_st1 = c << create_waveguide_straight(0.2,w,37,4)
d_st2 = c << create_waveguide_straight(1,w,37,4)
d_st3 = c << create_waveguide_straight(0.2,w,37,4)
d_b1 = c << create_waveguide_bend(30,w,16,37,4)
d_b2 = c << create_waveguide_bend(30,w,16,37,4)
d_b3 = c << create_waveguide_bend(r,w,a,37,4)
d_st4 = c << create_waveguide_straight(175.5,w,37,4)
d_b4 = c << create_waveguide_bend(r,w,a,37,4)
d_st5 = c << create_waveguide_straight(935,w,37,4)
d_b5 = c << create_waveguide_bend(r,w,a,37,4)
d_st6 = c << create_waveguide_straight(0.2,w,37,4)
d_st7 = c << create_waveguide_straight(0.2,w,37,4)

x1 = c << create_x(37,4)
x2 = c << create_x(37,4)
x3 = c << create_x(37,4)
x4 = c << create_x(37,4)
#taper cladding
u_taper1c = c << gf.components.straight(length=10, width=4.5, layer=(37,5))
u_taper2c = c << gf.components.straight(length=10, width=4.5, layer=(37,5))
d_taper1c = c << gf.components.straight(length=10, width=4.5, layer=(37,5))
d_taper2c = c << gf.components.straight(length=10, width=4.5, layer=(37,5))

#-----------add_ports------------
utaper1_p = add_ports(u_taper1)
utaper2_p = add_ports(u_taper2)
dtaper1_p = add_ports(d_taper1)
dtaper2_p = add_ports(d_taper2)

utaper1c_p = add_ports(u_taper1c)
utaper2c_p = add_ports(u_taper2c)
dtaper1c_p = add_ports(d_taper1c)
dtaper2c_p = add_ports(d_taper2c)

wg_rst1_p = add_ports(wg_rst1)
wg_rst2_p = add_ports(wg_rst2)
wg_rb1_p = add_ports(wg_rb1)
wg_rst3_p = add_ports(wg_rst3)
wg_rb2_p = add_ports(wg_rb2)
wg_rst4_p = add_ports(wg_rst4)
wg_rst5_p = add_ports(wg_rst5)
wg_rst6_p = add_ports(wg_rst6)

wg_lst1_p = add_ports(wg_lst1)
wg_lst2_p = add_ports(wg_lst2)
wg_lb1_p = add_ports(wg_lb1)
wg_lst3_p = add_ports(wg_lst3)
wg_lb2_p = add_ports(wg_lb2)
wg_lst4_p = add_ports(wg_lst4)
wg_lst5_p = add_ports(wg_lst5)
wg_lst6_p = add_ports(wg_lst6)

mmi1_p = add_ports(mmi1)

wg_st1_p = add_ports(wg_st1)
wg_st2_p = add_ports(wg_st2)
wg_st3_p = add_ports(wg_st3)
wg_b1_p = add_ports(wg_b1)
wg_b2_p = add_ports(wg_b2)
wg_st4_p = add_ports(wg_st4)
wg_b3_p = add_ports(wg_b3)
wg_st5_p = add_ports(wg_st5)
wg_b4_p = add_ports(wg_b4)
wg_st6_p = add_ports(wg_st6)
wg_b5_p = add_ports(wg_b5)
wg_st7_p = add_ports(wg_st7)
wg_st8_p = add_ports(wg_st8)
wg_st9_p = add_ports(wg_st9)

u_st1_p = add_ports(u_st1)
u_st2_p = add_ports(u_st2)
u_b1_p = add_ports(u_b1)
u_st3_p = add_ports(u_st3)
u_b2_p = add_ports(u_b2)
u_st4_p = add_ports(u_st4)
u_b3_p = add_ports(u_b3)
u_st5_p = add_ports(u_st5)
u_b4_p = add_ports(u_b4)
u_st6_p = add_ports(u_st6)
u_st7_p = add_ports(u_st7)

mmi2_p = add_ports(mmi2)

d_lst1_p = add_ports(d_lst1)
d_lst2_p = add_ports(d_lst2)
d_lst3_p = add_ports(d_lst3)
d_lst4_p = add_ports(d_lst4)
d_lb1_p = add_ports(d_lb1)
d_lst5_p = add_ports(d_lst5)
d_lb2_p = add_ports(d_lb2)
d_lb3_p = add_ports(d_lb3)
d_lst6_p = add_ports(d_lst6)
d_lb4_p = add_ports(d_lb4)
d_lb5_p = add_ports(d_lb5)
d_lst7_p = add_ports(d_lst7)
d_lb6_p = add_ports(d_lb6)
d_lst8_p = add_ports(d_lst8)
d_lst9_p = add_ports(d_lst9)


d_rst1_p = add_ports(d_rst1)
d_rst2_p = add_ports(d_rst2)
d_rst3_p = add_ports(d_rst3)
d_rst4_p = add_ports(d_rst4)
d_rb1_p = add_ports(d_rb1)
d_rst5_p = add_ports(d_rst5)
d_rb2_p = add_ports(d_rb2)
d_rb3_p = add_ports(d_rb3)
d_rst6_p = add_ports(d_rst6)
d_rb4_p = add_ports(d_rb4)
d_rb5_p = add_ports(d_rb5)
d_rst7_p = add_ports(d_rst7)
d_rb6_p = add_ports(d_rb6)
d_rst8_p = add_ports(d_rst8)
d_rst9_p = add_ports(d_rst9)

d_st1_p = add_ports(d_st1)
d_st2_p = add_ports(d_st2)
d_st3_p = add_ports(d_st3)
d_b1_p = add_ports(d_b1)
d_b2_p = add_ports(d_b2)
d_b3_p = add_ports(d_b3)
d_st4_p = add_ports(d_st4)
d_b4_p = add_ports(d_b4)
d_st5_p = add_ports(d_st5)
d_b5_p = add_ports(d_b5)
d_st6_p = add_ports(d_st6)
d_st7_p = add_ports(d_st7)

#-----------connect------------
wg_rst6.connect('o1', destination=mmi1['o2'])
wg_rst5.connect('o1', destination=wg_rst6['o2'])
wg_rst4.connect('o1', destination=wg_rst5['o2'])
wg_rb2.connect('o1', destination=wg_rst4['o2'])
wg_rst3.connect('o1', destination=wg_rb2['o2'])
wg_rb1.connect('o2', destination=wg_rst3['o2'])
wg_rst2.connect('o1', destination=wg_rb1['o1'])
wg_rst1.connect('o1', destination=wg_rst2['o2'])
u_taper1.connect('o1', destination=wg_rst1['o2'])
u_taper1c.connect('o1', destination=wg_rst1['o2'])
box1.connect('o1', destination=u_taper1c['o2'])


wg_lst6.connect('o1', destination=mmi1['o3'])
wg_lst5.connect('o1', destination=wg_lst6['o2'])
wg_lst4.connect('o1', destination=wg_lst5['o2'])
wg_lb2.connect('o2', destination=wg_lst4['o2'])
wg_lst3.connect('o1', destination=wg_lb2['o1'])
wg_lb1.connect('o1', destination=wg_lst3['o2'])
wg_lst2.connect('o1', destination=wg_lb1['o2'])
wg_lst1.connect('o1', destination=wg_lst2['o2'])
u_taper2.connect('o1', destination=wg_lst1['o2'])
u_taper2c.connect('o1', destination=wg_lst1['o2'])
box2.connect('o1', destination=u_taper2c['o2'])

wg_st1.connect('o1', destination=mmi1['o1'])
wg_st2.connect('o1', destination=wg_st1['o2'])
wg_st3.connect('o1', destination=wg_st2['o2'])
wg_b1.connect('o1', destination=wg_st3['o2'])
wg_b2.connect('o2', destination=wg_b1['o2'])
wg_st4.connect('o1', destination=wg_b2['o1'])
wg_b3.connect('o2', destination=wg_st4['o2'])
wg_st5.connect('o1', destination=wg_b3['o1'])
wg_b4.connect('o2', destination=wg_st5['o2'])
wg_st6.connect('o1', destination=wg_b4['o1'])
wg_b5.connect('o1', destination=wg_st6['o2'])
wg_st7.connect('o1', destination=wg_b5['o2'])
wg_st8.connect('o1', destination=wg_st7['o2'])
wg_st9.connect('o1', destination=wg_st8['o2'])
x1.connect('t1p2', destination=wg_st9['o2'])

u_st2.connect('o1', destination=u_st1['o1'])
u_b1.connect('o2', destination=u_st2['o2'])
u_st3.connect('o1', destination=u_b1['o1'])
u_b2.connect('o1', destination=u_st3['o2'])
u_st4.connect('o1', destination=u_b2['o2'])
u_b3.connect('o1', destination=u_st4['o2'])
u_st5.connect('o1', destination=u_b3['o2'])
u_b4.connect('o2', destination=u_st5['o2'])
u_st6.connect('o1', destination=u_b4['o1'])
u_st7.connect('o1', destination=u_st6['o2'])
x2.connect('t1p2', destination=u_st1['o2'])
x3.connect('t1p2', destination=u_st7['o2'])

d_lst1.connect('o1', destination=mmi2['o2'])
d_lst2.connect('o1', destination=d_lst1['o2'])
d_lst3.connect('o1', destination=d_lst2['o2'])
d_lst4.connect('o1', destination=d_lst3['o2'])
d_lb1.connect('o1', destination=d_lst4['o2'])
d_lst5.connect('o1', destination=d_lb1['o2'])
d_lb2.connect('o2', destination=d_lst5['o2'])
d_lb3.connect('o2', destination=d_lb2['o1'])
d_lst6.connect('o1', destination=d_lb3['o1'])
d_lb4.connect('o1', destination=d_lst6['o2'])
d_lb5.connect('o1', destination=d_lb4['o2'])
d_lst7.connect('o1', destination=d_lb5['o2'])
d_lb6.connect('o2', destination=d_lst7['o2'])
d_lst8.connect('o1', destination=d_lb6['o1'])
d_lst9.connect('o1', destination=d_lst8['o2'])
d_taper1.connect('o1', destination=d_lst9['o2'])
d_taper1c.connect('o1', destination=d_lst9['o2'])

d_rst1.connect('o1', destination=mmi2['o3'])
d_rst2.connect('o1', destination=d_rst1['o2'])
d_rst3.connect('o1', destination=d_rst2['o2'])
d_rst4.connect('o1', destination=d_rst3['o2'])
d_rb1.connect('o2', destination=d_rst4['o2'])
d_rst5.connect('o1', destination=d_rb1['o1'])
d_rb2.connect('o1', destination=d_rst5['o2'])
d_rb3.connect('o1', destination=d_rb2['o2'])
d_rst6.connect('o1', destination=d_rb3['o2'])
d_rb4.connect('o2', destination=d_rst6['o2'])
d_rb5.connect('o2', destination=d_rb4['o1'])
d_rst7.connect('o1', destination=d_rb5['o1'])
d_rb6.connect('o1', destination=d_rst7['o2'])
d_rst8.connect('o1', destination=d_rb6['o2'])
d_rst9.connect('o1', destination=d_rst8['o2'])
d_taper2.connect('o1', destination=d_rst9['o2'])
d_taper2c.connect('o1', destination=d_rst9['o2'])

d_st1.connect('o1', destination=mmi2['o1'])
d_st2.connect('o1', destination=d_st1['o2'])
d_st3.connect('o1', destination=d_st2['o2'])
d_b1.connect('o2', destination=d_st3['o2'])
d_b2.connect('o1', destination=d_b1['o1'])
d_b3.connect('o2', destination=d_b2['o2'])
d_st4.connect('o1', destination=d_b3['o1'])
d_b4.connect('o2', destination=d_st4['o2'])
d_st5.connect('o1', destination=d_b4['o1'])
d_b5.connect('o1', destination=d_st5['o2'])
d_st6.connect('o1', destination=d_b5['o2'])
d_st7.connect('o1', destination=d_st6['o2'])
x4.connect('t1p2', destination=d_st7['o2'])

#layer (13/1),(13/9),(14/11)
rectangle1 = c << create_rectangle(60, 80, 13, 1)
rectangle1 = move_rotate(rectangle1, -225, -10, 0)

rectangle2 = c << create_rectangle(60, 80, 13, 1)
rectangle2 = move_rotate(rectangle2, -125, -10, 0)

rectangle3 = c << create_rectangle(60, 80, 13, 1)
rectangle3 = move_rotate(rectangle3, -25, -10, 0)

rectangle4 = c << create_rectangle(60, 80, 13, 1)
rectangle4 = move_rotate(rectangle4, 75, -10, 0)

rectangle5 = c << create_rectangle(60, 80, 13, 1)
rectangle5 = move_rotate(rectangle5, 175, -10, 0)

rectangle6 = c << create_rectangle(60, 80, 13, 1)
rectangle6 = move_rotate(rectangle6, -225, -1830, 0)

rectangle7 = c << create_rectangle(60, 80, 13, 1)
rectangle7 = move_rotate(rectangle7, -125, -1830, 0)

rectangle8 = c << create_rectangle(60, 80, 13, 1)
rectangle8 = move_rotate(rectangle8, -25, -1830, 0)

rectangle9 = c << create_rectangle(60, 80, 13, 1)
rectangle9 = move_rotate(rectangle9, 75, -1830, 0)

rectangle10 = c << create_rectangle(60, 80, 13, 1)
rectangle10 = move_rotate(rectangle10, 175, -1830, 0)

Taper1 = c << create_taper(100, 312.3, 460, 13, 9)
Taper1 = move_rotate(Taper1, 5, -110, 90)

Taper2 = c << create_taper(100, 312.3, 460, 13, 9)
Taper2 = move_rotate(Taper2, 5, -1650, 270)

Taper3 = c << create_taper(100, 5.5, 60, 13, 9)
Taper3 = move_rotate(Taper3, -95, -110, 90)

Taper4 = c << create_taper(100, 187.7, 60, 13, 9)
Taper4 = move_rotate(Taper4, 5, -110, 90)

Taper5 = c << create_taper(100, 5.5, 60, 13, 9)
Taper5 = move_rotate(Taper5, 105, -110, 90)

Taper6 = c << create_taper(100, 5.5, 60, 13, 9)
Taper6 = move_rotate(Taper6, -95, -1650, 270)

Taper7 = c << create_taper(100, 187.7, 60, 13, 9)
Taper7 = move_rotate(Taper7, 5, -1650, 270)

Taper8 = c << create_taper(100, 5.5, 60, 13, 9)
Taper8 = move_rotate(Taper8, 105, -1650, 270)

waveguide1 = c << create_waveguide_straight(1540, 112, 13, 9)
waveguide1 = move_rotate(waveguide1, -95.15, -1650, 90)

waveguide2 = c << create_waveguide_straight(1540, 112, 13, 9)
waveguide2 = move_rotate(waveguide2, 105.15, -1650, 90)

parallelogram1 = c.add_polygon([(-151.15, -110),(-101.15, -110),(-165, -10),(-225, -10)],layer=(13, 9))
parallelogram2 = c.add_polygon([(111.15, -110),(161.15, -110),(235, -10),(185, -10)],layer=(13, 9))
parallelogram3 = c.add_polygon([(-225, -1750),(-165, -1750),(-101.15, -1650),(-151.15, -1650)],layer=(13, 9))
parallelogram4 = c.add_polygon([(185, -1750),(235, -1750),(161.15, -1650),(111.15, -1650)],layer=(13, 9))

Circle = create_circle(0.155, 14, 11)
circle1_array = c << create_array(Circle, 0.6, 0.6, 3, 58)
circle1_array = move_rotate(circle1_array, -166.5, 12.9, 0)

circle2_array = c << create_array(Circle, 0.6, 0.6, 3, 58)
circle2_array = move_rotate(circle2_array, -123.5, 12.9, 0)

circle3_array = c << create_array(Circle, 0.6, 0.6, 3, 58)
circle3_array = move_rotate(circle3_array, -66.5, 12.9, 0)

circle4_array = c << create_array(Circle, 0.6, 0.6, 3, 58)
circle4_array = move_rotate(circle4_array, -23.5, 12.9, 0)

circle5_array = c << create_array(Circle, 0.6, 0.6, 3, 58)
circle5_array = move_rotate(circle5_array, 33.5, 12.9, 0)

circle6_array = c << create_array(Circle, 0.6, 0.6, 3, 58)
circle6_array = move_rotate(circle6_array, 76.5, 12.9, 0)

circle7_array = c << create_array(Circle, 0.6, 0.6, 3, 58)
circle7_array = move_rotate(circle7_array, 133.5, 12.9, 0)

circle8_array = c << create_array(Circle, 0.6, 0.6, 3, 58)
circle8_array = move_rotate(circle8_array, 176.5, 12.9, 0)

circle9_array = c << create_array(Circle, 0.6, 0.6, 3, 2500)
circle9_array = move_rotate(circle9_array, -102.65, -1629.7, 0)

circle10_array = c << create_array(Circle, 0.6, 0.6, 3, 2500)
circle10_array = move_rotate(circle10_array, -97.45, -1629.7, 0)

circle11_array = c << create_array(Circle, 0.6, 0.6, 3, 2500)
circle11_array = move_rotate(circle11_array, 97.35, -1629.7, 0)

circle12_array = c << create_array(Circle, 0.6, 0.6, 3, 2500)
circle12_array = move_rotate(circle12_array, 102.55, -1629.7, 0)


c.plot()
c.show()