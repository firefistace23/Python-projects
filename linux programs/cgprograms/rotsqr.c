#include<stdio.h>
#include<math.h>
#include<GL/glut.h>

void init()
{
	glClearColor(1.0,1.0,1.0,0.0);
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(0.0,500.0,0.0,500.0);
}

int x,y,s;


void square()
{
	glBegin(GL_QUADS);
		glVertex2f(x,y);
		glVertex2f(x+s,y);
		glVertex2f(x+s,y+s);
		glVertex2f(x,y+s);
	glEnd();
}

void draw()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0.0,0.0,0.0);
	square();
	glutSwapBuffers();
	
}

void spinS()
{
	if(x<500-s)
	x=x+2;

	glutPostRedisplay();

}

void mouseF(int btn,int state,int x,int y)
{
	if(btn==GLUT_LEFT_BUTTON && state==GLUT_DOWN)
		glutIdleFunc(spinS);
	if(btn==GLUT_RIGHT_BUTTON && state==GLUT_DOWN)
		glutIdleFunc(NULL);
}

void main(int argc, char** argv)
{
	glutInit(&argc,argv);
	printf("enter position of square and side");
	scanf("%d%d%d",&x,&y,&s);

	glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB);
	glutInitWindowPosition(0.0,0.0);
	glutInitWindowSize(500.0,500.0);
	glutCreateWindow("Rotate Triangle");
	init();
	glutDisplayFunc(draw);
	glutIdleFunc(spinS);
	glutMouseFunc(mouseF);
	glutMainLoop();
	
}
