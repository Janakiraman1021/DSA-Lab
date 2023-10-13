import java.util.*;

abstract class Shape {
    int a, b;
    abstract public void printArea();
}

class Rectangle extends Shape {
    public int areaRect;

    public void printArea() {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter the length and breadth of the rectangle");
        a = s.nextInt();
        b = s.nextInt();
        areaRect = a * b;
        System.out.println("Length of rectangle: " + a);
        System.out.println("Breadth of rectangle: " + b);
        System.out.println("The area of rectangle is: " + areaRect);
    }
}

class Triangle extends Shape {
    double areaTri;

    public void printArea() {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter the base and height of the triangle");
        a = s.nextInt();
        b = s.nextInt();
        System.out.println("Base of triangle: " + a);
        System.out.println("Height of triangle: " + b);
        areaTri = 0.5 * a * b;
        System.out.println("The area of the triangle is: " + areaTri);
    }
}

class Circle extends Shape {
    double areaCircle;

    public void printArea() {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter the radius of the circle");
        a = s.nextInt();
        areaCircle = 3.14 * a * a;
        System.out.println("Radius of circle: " + a);
        System.out.println("The area of the circle is: " + areaCircle);
    }
}

public class ShapeClass {
    public static void main(String[] args) {
        Rectangle r = new Rectangle();
        r.printArea();

        Triangle t = new Triangle();
        t.printArea();

        Circle c = new Circle();
        c.printArea();
    }
}
