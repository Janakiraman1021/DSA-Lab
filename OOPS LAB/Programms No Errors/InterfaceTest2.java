interface Area {
    float pi = 3.14F;

    float compute(float x, float y);
}

class Rectangle implements Area {
    public float compute(float x, float y) {
        return (x * y);
    }
}


class Circle implements Area {
    public float compute(float x, float y) {
        return (pi * x * x);
    }
}

class Triangle implements Area {
    public float compute(float x, float y) {
        return ((x * y) / 2);
    }
}

public class InterfaceTest2{
    public static void main(String args[]) {
        Rectangle rect = new Rectangle();
        Circle cir = new Circle();
        Triangle tr = new Triangle();
        Area a;

        a = rect;
        System.out.println("Area of rectangle: " + a.compute(5, 10));

        a = cir;
        System.out.println("Area of circle: " + a.compute(5, 0));

        a = tr;
        System.out.println("Area of Triangle: " + a.compute(5, 7));
    }
}
