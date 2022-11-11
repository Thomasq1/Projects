//Thomas O'Brien R00192530
package application;


import javafx.stage.Stage;
import javafx.stage.Modality;
import javafx.scene.Scene;
import javafx.scene.layout.VBox;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.geometry.Pos;

public class popup {
//	private static Controller StudentController = new Controller();
	
	public static void display(String title, String message) { 
		
//code to display a popup box when the user clicks exit on the program		
		Stage window = new Stage();
		
		window.initModality(Modality.APPLICATION_MODAL);
		window.setTitle(title);
		window.setMinWidth(250);
		
		Label label = new Label();
		label.setText(message);
		
		Button exitButton = new Button("Exit");
		exitButton.setOnAction(e -> System.exit(0));
		
//		Button saveButton = new Button("Save");
//		saveButton.setOnAction(e -> {
//			StudentController.saveFile();
//	    	System.out.println("file saved successfully ");
//	    	System.exit(0);
//		});
		
		VBox layout = new VBox(10);
		layout.getChildren().addAll(label, exitButton);
		layout.setAlignment(Pos.CENTER);
		
		
		Scene scene = new Scene(layout);
		window.setScene(scene);
		window.showAndWait();
		}
	}
