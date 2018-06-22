#include<stdio.h>
#include<GL/glut.h>
#include<math.h>

void init()
{
	glClearColor(1,1,1,0);
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(0,500,0,500);
}
int t=0,angle=0;

float pi=3.14;
void draww()
{
	int xc=50,yc=50,r=40;
	glBegin(GL_POINTS);
	float t;
	for(int i=0;i<360;i++)
	{
	t=i*pi/180;
	glVertex2d((xc+r*cos(t)),(yc+r*sin(t)));
	}
	glEnd();
	glBegin(GL_LINES);
	glVertex2d(50,90);
	glVertex2d(50,10);
	glVertex2d(10,50);
	glVertex2d(90,50);
	glEnd();
}

void disp()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0,0,0);
	glBegin(GL_LINES);
	glVertex2d(0,10);
	glVertex2d(500,10);
	glEnd();

	glPushMatrix();
	glTranslated(t,0,1);
	glTranslated(50,50,0);
	glRotated(-angle,0,0,1);
	glTranslated(-50,-50,0);
	draww();
	glPopMatrix();

	glutSwapBuffers();
	glFlush();
	
}

void keyfn(unsigned char k,int x,int y)
{
	if(k=='d')
	{t++;angle++;
	}
	if(k=='a')
	{t--;angle--;}
	disp();
	
}


void main(int argc,char** argv)
{
	glutInit(&argc,argv);
	glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB);

	glutInitWindowPosition(0,0);
	glutInitWindowSize(500,500);
	
	glutCreateWindow("Wheele");
	init();
	glutDisplayFunc(disp);
	glutKeyboardFunc(keyfn);
	glutMainLoop();

}
