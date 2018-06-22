#include<stdio.h>
#include<math.h>
#include<GL/glut.h>

void init()
{
	glClearColor(1.0,1.0,1.0,0.0);
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(-250.0,250.0,-250.0,250.0);
}

int a,b,r;
double pi=3.14,c;
void draw(int a,int b,int r)
{
	for(int t=0;t<360;t++)
	{
	c=t*pi/180;
	glVertex2d(a+r*cos(c),b+r*sin(c));
	}
}

void pcircle()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0.0,0.0,0.0);
	glBegin(GL_POINTS);
	draw(a,b,r);
	glEnd();
	glFlush();
}



void main(int argc,char **argv)
{
	glutInit(&argc,argv);
	printf("enter center and radius");
	scanf("%d%d%d",&a,&b,&r);



	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
	glutInitWindowPosition(0.0,0.0);
	glutInitWindowSize(500.0,500.0);
	glutCreateWindow("Polar Circle Drawing");
	init();
	glutDisplayFunc(pcircle);
	glutMainLoop();
}
