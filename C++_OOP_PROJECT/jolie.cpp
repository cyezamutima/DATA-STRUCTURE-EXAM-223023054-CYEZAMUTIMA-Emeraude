#include <iostream>
#include <cmath> 
using namespace std;
struct Point {
    float x, y;
};
class Shape {
public:
    virtual float area() = 0;         
    virtual void drawASCII() = 0;     
    virtual ~Shape() {}
};
class Rectangle : public Shape {
    float* width;
    float* height;
public:
    Rectangle(float w, float h) {
        width = new float(w);     
        height = new float(h);    
    }
    float area() {
        return (*width) * (*height); 
    }

    void drawASCII() {
        int w = (int)(*width);
        int h = (int)(*height);
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                cout << "*";
            }
            cout << "\n";
        }
    }
    ~Rectangle() {
        delete width;
        delete height;
    }
};
class Circle : public Shape {
    float* radius;
public:
    Circle(float r) {
        radius = new float(r);  
    }

    float area() {
        return 3.14f * (*radius) * (*radius); 
    }

    void drawASCII() {
        cout << "  ***  \n";
        cout << " *   * \n";
        cout << " *   * \n";
        cout << "  ***  \n";
    }

    ~Circle() {
        delete radius;
    }
};
class Triangle : public Shape {
    Point* vertices;
public:
    Triangle(Point a, Point b, Point c) {
        vertices = new Point[3];  
        vertices[0] = a;
        vertices[1] = b;
        vertices[2] = c;
    }
    float area() {
        return 0.5f * abs(
            vertices[0].x * (vertices[1].y - vertices[2].y) +
            vertices[1].x * (vertices[2].y - vertices[0].y) +
            vertices[2].x * (vertices[0].y - vertices[1].y)
        );
    }
    void drawASCII() {
        cout << "  *  \n";
        cout << " * * \n";
        cout << "*****\n";
    }
    ~Triangle() {
        delete[] vertices;
    }
};
Shape** shapes = NULL; 
int shapeCount = 0;     
void addShape(Shape* newShape) {
    Shape** newArray = new Shape*[shapeCount + 1];
    for (int i = 0; i < shapeCount; i++) {
        newArray[i] = shapes[i];  
    }
    newArray[shapeCount] = newShape; 
    delete[] shapes;   
    shapes = newArray; 
    shapeCount++;
}
int main() {
    addShape(new Rectangle(5, 3));
    addShape(new Circle(3));
    Point a = {0, 0}, b = {4, 0}, c = {0, 3};
    addShape(new Triangle(a, b, c));
    for (int i = 0; i < shapeCount; i++) {
        cout << "Shape " << (i + 1) << ":\n";
        cout << "Area: " << shapes[i]->area() << "\n";
        shapes[i]->drawASCII();
        cout << "------------------------\n";
    }
    for (int i = 0; i < shapeCount; i++) {
        delete shapes[i];
    }
    delete[] shapes;

    return 0;
}

