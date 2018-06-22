#include<stdio.h>
#include<GL/glut.h>
#include<math.h>

void init()
{
	glClearColor(1.0,1.0,1.0,0.0);
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(0.0,500.0,0.0,500.0);	
}

int a,b,s;

void square()
{
	glBegin(GL_LINE_LOOP);
		glVertex2f(a,b);
		glVertex2f(a+s,b);
		glVertex2f(a+s,b+s);
		glVertex2f(a,b+s);
	glEnd();
}

void bfill(int x,int y,float nc[3],float bc[3])
{
	float gc[3];
	while()
	glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT,&gc);
}

void draw()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0.1,0.0,0.0);
	float newc[3]={0.0,0.1,0.0);
	float bndc[3]={0.1,0.0,0.0}
	square();
	bfill(x,y,newc[3],bndc[3]);
	glFlush();
}

void main(int argc,char** argv)
{
	glutInit(&argc,argv);
	printf("enter position of square and side");
	scanf("%d%d%d",&a,&b,&s);
	
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
	glutInitWindowPosition(0.0,0.0);
	glutInitWindowSize(500.0,500.0);
	
	glutCreateWindow("Boundary Fill");
	init();
	glutDisplayFunc(draw);
	glutMainLoop();
}
