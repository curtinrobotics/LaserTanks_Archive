import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.KeyEvent;
import controlP5.*;
import java.util.*;
import processing.serial.*;// attaching the serial library into gamemaster UI for reading

Robot robot;
Serial MasterArduino;// creating a local serial object from the library
ControlP5  CP5;

ControlP5 Scroll;
ScrollableList NOP;
ScrollableList p1l1;

ControlP5 textin;
Textfield player1;
Textfield player2;
Textfield player3;
Textfield player4;

ControlP5 textshow;
Textlabel player_1;
Textlabel player_2;
Textlabel player_3;
Textlabel player_4;

ControlP5 slider;
Slider  time1;
Bang b1;

PImage Croc_logo;

int pop_up =0;
float i = 0;
int input;
int next1_button = 0;
int next2_button = 0;
int nameof_player=0;
String in_tank = null ; //variable to read and hold the information comming from the mega
String in_powerup = null; //variable to read and hold the information comming from the mega
int space = 32; // variable to seperate different info comming in to their invidual variable
int nl = 10;
boolean start_mode= false;

//initialize vars
String title = "Deathmatch";
String timeStr = "0:00";
int counter = 180000;
int timer = 0;
int startTime = 0;
int tSecs = 0;
boolean timing = false;
boolean mousePrevPressed = false;
boolean drop = false;

float it ;
int people;

String name = new String("");
float pos;

String player_name1= new String("");
String player_name2= new String("");
String player_name3= new String("");
String player_name4= new String("");

String url1, url2;

// initialize buttons
ArrayList<Button> buttons = new ArrayList<Button>();
Button plusButt = new Button(750, 55, 40, 40, #00ff00, "+",20);
Button minusButt = new Button(700, 55, 40, 40, #ff0000, "-",20);
Button startButt = new Button(618, 120, 100, 50, #ffff00, "Start",20);
Button exit = new Button(618, -1, 40,40, #ff0000, "X",20);
Button togame = new Button(1600, 100, 300, 60, #00ff00, "To Game",50);
Button tofreeforall = new Button((1920/2)-400/2, 400, 400, 60, #00ff00, "Free for all",50);
Button back_tff = new Button(100, 120, 100, 50, #00ff00, "Back",20);

Button p1enter = new Button(420, 500, 200, 50, #EA1717, "ENTER",30);
Button p2enter = new Button(820, 500, 200, 50, #00ff00, "ENTER",30);
Button p3enter = new Button(1220, 500, 200, 50, #6D6DF8, "ENTER",30);
Button p4enter = new Button(1630, 500, 200, 50, #FFFF00, "ENTER",30);
