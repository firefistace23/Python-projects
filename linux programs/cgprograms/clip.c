#include<stdio.h>
#include<math.h>
#include<GL/glut.h>

void init()
{
	glClearColor(1.0,1.0,1.0,0.0);
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(0.0,500.0,0.0,500.0);
}

int l,b,r,t,xa,ya,xb,yb;


float round_value(float v)
{
  return (v + 0.5);
}

void clipline(int X1,int Y1,int X2,int Y2)
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
		if(x<l||x>r||y<b||y>t)
		glVertex2d(round_value(x), round_value(y));
	  }
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

void clipLine()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0.0,0.0,0.0);
	glBegin(GL_POINTS);
	
	dline(l,b,r,b);
	dline(l,b,l,t);
	dline(l,t,r,t);
	dline(r,t,r,b);
	clipline(xa,ya,xb,yb);

	glEnd();
	glFlush();
}



void main(int argc,char **argv)
{
	glutInit(&argc,argv);
	printf("enter end points of line segment");
	scanf("%d%d%d%d",&xa,&ya,&xb,&yb);
	printf("enter left bottom and right top corners of clip rectangle");
	scanf("%d%d%d%d",&l,&b,&r,&t);
	


	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
	glutInitWindowPosition(0.0,0.0);
	glutInitWindowSize(500.0,500.0);
	glutCreateWindow("Clip Line");
	init();
	glutDisplayFunc(clipLine);
	glutMainLoop();
}
