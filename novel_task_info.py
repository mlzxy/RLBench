tasks = """basketball_in_hoop
beat_the_buzz
block_pyramid
change_channel
change_clock
close_box
close_door
close_drawer
close_fridge
close_grill
close_jar
close_laptop_lid
close_microwave
empty_container
empty_dishwasher
get_ice_from_fridge
hang_frame_on_hanger
hit_ball_with_queue
hockey
insert_usb_in_computer
lamp_off
lamp_on
light_bulb_out
meat_on_grill
move_hanger
open_box
open_door
open_fridge
open_grill
open_jar
open_microwave
open_oven
open_window
open_wine_bottle
phone_on_base
pick_and_lift
pick_up_cup
place_hanger_on_rack
play_jenga
plug_charger_in_power_supply
pour_from_cup_to_cup
press_switch
put_books_at_shelf_location
put_books_on_bookshelf
put_bottle_in_fridge
put_knife_in_knife_block
put_knife_on_chopping_board
put_plate_in_colored_dish_rack
put_rubbish_in_bin
put_rubbish_in_color_bin
put_shoes_in_box
put_toilet_roll_on_stand
put_tray_in_oven
put_umbrella_in_umbrella_stand
reach_target
remove_cups
scoop_with_spatula
screw_nail
set_clock_to_time
set_the_table
setup_checkers
setup_chess
slide_cabinet_open_and_place_cups
slide_cabinet_open
solve_puzzle
stack_wine
straighten_rope
take_cup_out_from_cabinet
take_frame_off_hanger
take_item_out_of_drawer
take_lid_off_saucepan
take_money_out_safe
take_off_weighing_scales
take_plate_off_colored_dish_rack
take_shoes_out_of_box
take_toilet_roll_off_stand
take_tray_out_of_oven
take_umbrella_out_of_umbrella_stand
take_usb_out_of_computer
toilet_seat_down
toilet_seat_up
turn_oven_on
tv_on
unplug_charger
water_plants
weighing_scales
wipe_desk""".split('\n')


for t in tasks:
    with open(f"/home/xinyu/Workspace/RVT/rlbench/rlbench/tasks/{t}.py") as f:
        lines = f.readlines()
    LINE = None
    for i, l in enumerate(lines):
        if 'variation_count' in l:
            LINE = lines[i+1]
    assert LINE is not None
    v = LINE.split('return')[-1].strip()
    print(f"{t}\t{v}")

        