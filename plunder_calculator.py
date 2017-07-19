print('OGame Plunder Calculator v0.2')
print('Copyright (c) 2017 Diogo Queiroz. All Rights Reserved.')

# -*- coding: UTF-8 -*-

again=1

while again == 1:
    econ_speed=4    #economy speed
    fleet_speed=2   #fleet speed
    combustion_tech=6
    impulsion_tech=3
    sc_cap=5000     #small cargo capacity
    lc_cap=25000    #lage cargo capacity
    sc_speed=5000*(1+0.1*combustion_tech)   #small cargo speed
    lc_speed=7500*(1+0.2*impulsion_tech)   #large cargo speed
    home_sys=272    #home solar system number
    home_pl=12      #home planet number

    c_res=int(input('\n\nCurrent resources: '))
    honor=int(input('Honor (%): '))
    m_lvl=int(input('Metal level: '))
    c_lvl=int(input('Crystal level: '))
    d_lvl=int(input('Deuterium level: '))
    target_sys=int(input('Target Solar System: '))

    #distance calculation
    if (target_sys == home_sys):
        target_pl=int(input('Target planet: '))
        dist=1000+5*abs((home_pl-target_pl))
    else:
        dist=2700+95*abs((home_sys-target_sys))

    flight_time=(10+3500*((10*dist)/sc_speed)**(1/2))/fleet_speed

    #production per second
    m_prod_sec=((econ_speed*30*m_lvl*(1.1**m_lvl))+(econ_speed*30))/3600
    c_prod_sec=((econ_speed*20*c_lvl*(1.1**c_lvl))+(econ_speed*15))/3600
    d_prod_sec=(econ_speed*(10*d_lvl*(1.1**d_lvl))*1.36)/3600

    av_res=(c_res+flight_time*(m_prod_sec+c_prod_sec+d_prod_sec)*0.01*honor)
    req_sc_ships=av_res/5000
    req_lc_ships=av_res/25000

    print('\n\nBy the time you arrive, you should be able to plunder {}'.format(int(av_res)))
    print('In order to do so, you\'ll need:')
    print('\n{:03.2f} Small Cargo Ships'.format(req_sc_ships))
    print('or')
    print('{:03.2f} Large Cargo Ships'.format(req_lc_ships))
    print('\nin order to be able to plunder all available resources')

    q=input('\n\nRun again? (y/n)')

    if (q=='n'): again=0


input("\n\nPress the enter key to exit.")