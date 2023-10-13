package application;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

public class MenuExample extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    public void start(Stage primaryStage) throws Exception {
        BorderPane root = new BorderPane();
        Scene scene = new Scene(root, 200, 300);
        MenuBar menuBar = new MenuBar();
        Menu fileMenu = new Menu("File");
        MenuItem fileMenu1 = new MenuItem("New");
        MenuItem fileMenu2 = new MenuItem("Save");
        MenuItem fileMenu3 = new MenuItem("Exit");
        Menu editMenu = new Menu("Edit");
        MenuItem editMenu1 = new MenuItem("Cut");
        MenuItem editMenu2 = new MenuItem("Copy");
        MenuItem editMenu3 = new MenuItem("Paste");
        editMenu.getItems().addAll(editMenu1, editMenu2, editMenu3);
        root.setTop(menuBar);
        fileMenu.getItems().addAll(fileMenu1, fileMenu2, fileMenu3);
        menuBar.getMenus().addAll(fileMenu, editMenu);
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
