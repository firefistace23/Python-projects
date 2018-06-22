#include<stdio.h>
#include<math.h>
#include<GL/glut.h>

void init()
{
	glClearColor(1.0,1.0,1.0,0.0);
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(0.0,600.0,0.0,600.0);
}

int x,y;

void floodFill(int x,int y,float oc[3],float nc[3])
{
	float gc[3];
	glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT,&gc);
	if(gc[0]==oc[0]&&gc[1]==oc[1]&&gc[2]==oc[2])
	{
		glColor3f(nc[0],nc[1],nc[2]);
		glBegin(GL_POINTS);
		glVertex2d(x,y);
		glEnd();
		floodFill(x+1,y,oc,nc);
		floodFill(x,y+1,oc,nc);
		floodFill(x-1,y,oc,nc);
		floodFill(x,y-1,oc,nc);
	}
}


void Flood()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0.0,0.0,0.0);
	
	float oldc[3]={1.0,1.0,1.0};
	float newc[3]={1.0,0.0,0.0};

	glBegin(GL_LINES);
		glVertex2i(20,20);
		glVertex2i(20,100);
		glVertex2i(20,100);
		glVertex2i(100,100);
		glVertex2i(100,100);
		glVertex2i(100,20);
		glVertex2i(100,20);
		glVertex2i(20,20);
	glEnd();
	

	floodFill(x,y,oldc,newc);

	
	glFlush();
}




void main(int argc,char **argv)
{
	glutInit(&argc,argv);
	

	printf("enter start point ");
	scanf("%d%d",&x,&y);


	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
	glutInitWindowPosition(0.0,0.0);
	glutInitWindowSize(600.0,600.0);
	glutCreateWindow("F FILL");
	init();
	glutDisplayFunc(Flood);
	glutMainLoop();
}
