#include<stdio.h>
#include<math.h>
#include<GL/glut.h>

void init()
{
	glClearColor(1.0,1.0,1.0,0.0);
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(0.0,500.0,0.0,500.0);
}

int p1,q1,p2,q2,p3,q3,rx,ry;
double pi=3.14,t;

float round_value(float v)
{
  return (v + 0.5);
}

void dline(int X1,int Y1,int X2,int Y2)
{
	  double dx=(X2-X1);
	  double dy=(Y2-Y1);
	  double steps;
	  float xInc,yInc,x=X1,y=Y1;
	  steps=(abs(dx)>abs(dy))?(abs(dx)):(abs(dy));
	  xInc=dx/(float)steps;
	  yInc=dy/(float)steps;
	  glBegin(GL_POINTS);
	  glVertex2d(x,y);
	  int k;
	  
	  for(k=0;k<steps;k++)
	  {
		x+=xInc;
		y+=yInc;
		glVertex2d(round_value(x), round_value(y));
	  }
}


void draw()
{
	int P1,P2,P3,Q1,Q2,Q3;
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0.0,0.0,0.0);
	glBegin(GL_POINTS);
	dline(p1,q1,p2,q2);
	dline(p3,q3,p2,q2);
	dline(p1,q1,p3,q3);
	t=t*3.14/180;
	P1=(p1-rx)*cos(t)-(q1-ry)*sin(t)+rx;
	Q1=(q1-ry)*cos(t)+(p1-rx)*sin(t)+ry;
	P2=(p2-rx)*cos(t)-(q2-ry)*sin(t)+rx;
	Q2=(q2-ry)*cos(t)+(p2-rx)*sin(t)+ry;
	P3=(p3-rx)*cos(t)-(q3-ry)*sin(t)+rx;
	Q3=(q3-ry)*cos(t)+(p3-rx)*sin(t)+ry;
	printf("%d%d",P1,Q1);
	dline(P1,Q1,P2,Q2);
	dline(P3,Q3,P2,Q2);
	dline(P1,Q1,P3,Q3);
	glEnd();
	glFlush();
}



void main(int argc,char **argv)
{
	glutInit(&argc,argv);
	printf("enter coordinates of triangle");	
	scanf("%d%d%d%d%d%d",&p1,&q1,&p2,&q2,&p3,&q3);
	printf("enter theta and refpoint");
	scanf("%lf%d%d",&t,&rx,&ry);

	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
	glutInitWindowPosition(0.0,0.0);
	glutInitWindowSize(500.0,500.0);
	glutCreateWindow("Rotate Triangle");
	init();
	glutDisplayFunc(draw);
	glutMainLoop();
}
