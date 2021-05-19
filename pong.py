from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()
speed = 0.5
bat = [7,4]

up_down = -1

w = (0,0,0)
r = (255,0,0)
b = (0,0,255)
game_space = [w,w,w,w,w,w,w,w,
            w,w,w,w,w,w,w,w,
            w,w,w,w,w,w,w,w,
            w,w,w,w,w,w,w,w,
            w,w,w,w,w,w,w,w,
            w,w,w,w,w,w,w,w,
            w,w,w,w,w,w,w,w,
            w,w,w,b,b,w,w,w]

def set_color_on_point(x,y,col):
  game_space[get_right_most_point(x,y)] = col
  sense.set_pixels(game_space)
def get_right_most_point(x,y):
  point  = 8 * x + y
  return point
            
def update_space(x, y, colour):
  #index element from coordinate
  p = 8 * x + y
  game_space[p] = colour
  sense.set_pixels(game_space)
  
def left(event):
  if event.action == 'pressed':
    #the basket reached the left side
    if bat[0] == 7:
      if bat[1]-1 == 0:
        pass
      #move basket one position left
      else:
        # update_space(bat[0], bat[1], w)
        # bat[1] -= 1
        # update_space(bat[0], bat[1], b)
        # update_space(bat[0], bat[1] - 1, b)
        # update_space(bat[0], bat[1] - 2, b)
        # update_space(bat[0], bat[1] - 3, b)
        set_color_on_point(bat[0], bat[1], w)
        bat[1] -=1
        set_color_on_point(bat[0], bat[1], b)
        set_color_on_point(bat[0], bat[1] - 1, b)
      
def right(event):
  if event.action == 'pressed':
    #the basket reached the right side
    if bat[1] + 1 == 8:
      pass
    #move basket one position right
    else:
      # update_space(bat[0], bat[1] - 2, w)
      # bat[1] += 1
      # update_space(bat[0], bat[1], b)
      # update_space(bat[0], bat[1]+1, b)
      # update_space(bat[0], bat[1]+2, b)
      set_color_on_point(bat[0], bat[1] -1, w)
      bat[1] +=1
      set_color_on_point(bat[0], bat[1], b)
      set_color_on_point(bat[0], bat[1] - 1, b)
      
sense.stick.direction_left = left
sense.stick.direction_right = right

sense.clear()
sense.set_pixels(game_space)
game_alive = True

score = 0
game_speed_var = 0

bat_hit = False 
top_reached = True

while game_alive:
  #initialize position and direction of the ball
  #(x,y) – ball coordinate, d - direction
  
  if bat_hit:
    ball_x = 7
    ball_y = ball_y
  else:
    ball_x = 0
    ball_y = random.randint(0,7)
  
  pv = 0;
  s_inc = False
  # random.choice() – randomly selects a value from a list
  ball_d = random.choice([-1,1])
  #put the ball into the game space
  update_space(ball_x, ball_y, r)
  #while the ball is in the game space
  while True:
    if speed > 0:
      sleep(speed)
    else:
      break
    update_space(ball_x, ball_y, w)
    #ball is on the edge of x dimension
    if ball_x == 7:
      if ball_y == bat[1]-1 or ball_y == bat[1]:
        speed -= game_speed_var
        #ball is in the basket
        set_color_on_point(ball_x, ball_y, b)
        score += 1
        game_speed_var += 0.01
        bat_hit = True
        # break
      else:
        #ball is out of the space
        game_alive = False
        break
    #ball reached the right side of the space
    if ball_y == 7 and ball_d == 1:
      ball_d = -1
    #ball reached the left side of the space
    elif ball_y == 0 and ball_d == -1:
      ball_d = 1
    ball_y += ball_d
    if bat_hit:
      ball_x -= 1
      if ball_x == 0:
        bat_hit = False
    else:
      ball_x += 1
    # if ball_x == -8:
    #   bat_hit = False
    #   top_reached = True
    
    # print("x = {}, y = {}".format(ball_x,ball_y))
        
    update_space(ball_x, ball_y, r)

sense.clear()
sense.show_message('Game over!', scroll_speed=0.05, back_colour=w)
sense.show_message('Score: ' + str(score), scroll_speed=0.01,back_colour=w)