import gdsfactory as gf

#pcell
#grating coupler 생성 함수
def create_grating_coupler():
    gc = gf.components.grating_coupler_elliptical_te()
    return gc

#component move, rotate 함수
def move_rotate(com, x, y, angle):
    c = com
    c.rotate(angle)
    c.move(origin=(0,0), destination=(x,y))
    return c
#waveguide(straight) 생성 함수
def create_waveguide_straight(l, w, layer1, layer2):
    wg_st = gf.components.straight(length=l, width=w, layer=(layer1,layer2),cladding_layers=[(layer1,layer2+1)], cladding_offsets=[2])
    return wg_st
#waveguide(bend euler) 생성 함수
def create_waveguide_bend(r, w, a,layer1,layer2):
    wg_b = gf.components.bend_euler(radius=r, width=w, angle=a, npoints=720, layer=(layer1,layer2),cladding_layers=[(layer1,layer2+1)], cladding_offsets=[2])

    return wg_b
#mmi 생성 함수
def create_mmi(l,w):
    mmi = gf.components.mmi1x2(length_mmi=l,width_mmi=w,width_taper=3)
    return mmi
#circle 생성 함수
def create_circle(radius,layer1,layer2):
    circle = gf.components.circle(radius=radius, angle_resolution=18.5, layer=(layer1,layer2))
    return circle
#rectangle box 생성 함수
def create_rectangle(x,y,layer1,layer2):
    rectangle = gf.components.rectangle(size=[x,y], layer=(layer1,layer2))
    return rectangle
#사다리꼴 생성 함수
def create_taper(length,width1,width2,layer1,layer2):
    taper = gf.components.taper(length=length, width1=width1, width2=width2, layer=(layer1, layer2))
    return taper
#taper 생성 함수
def create_w_taper(length,width1,width2,layer1,layer2):
    taper = gf.components.taper(length=length, width1=width1, width2=width2, layer=(layer1, layer2),cladding_layers=[(layer1,layer2+1)], cladding_offsets=[2])
    return taper
#array 생성 함수
def create_array(com,x_distance,y_distance,column,row):
    array = gf.components.array(component=com, spacing=[x_distance, y_distance], columns=column, rows=row, add_ports=True)
    return array
#component에 port 생성 함수
def add_ports(name):
    base_name = name.name.split('(')[0]
    port_data = [(f'{base_name}_{i+1}', port_value) for i, (_, port_value) in enumerate(name.ports)]
    return port_data[0][0]
#이름모를도형 생성 함수
def create_x(layer1,layer2):
    c = gf.Component()
    taper1 = c << gf.components.taper(length=38, width1=19.26, width2=0.5,layer=(layer1,layer2),cladding_layers=[(layer1,layer2+1)], cladding_offsets=[2])
    taper2 = c << gf.components.taper(length=0.5, width1=19.31, width2=19.26,layer=(layer1,layer2),cladding_layers=[(layer1,layer2+1)], cladding_offsets=[2])
    taper3 = c << gf.components.taper(length=11, width1=19.31, width2=19.31,layer=(layer1,layer2),cladding_layers=[(layer1,layer2+1)], cladding_offsets=[2])
    c.add_port('t1p1', port=taper1['o1'])
    c.add_port('t1p2', port=taper1['o2'])
    c.add_port('t2p1', port=taper2['o1'])
    c.add_port('t2p2', port=taper2['o2'])
    c.add_port('t3p1', port=taper3['o1'])
    c.add_port('t3p2', port=taper3['o2'])
    taper2.connect('o2', destination=taper1['o1'])
    taper3.connect('o1', destination=taper2['o1'])
    return c