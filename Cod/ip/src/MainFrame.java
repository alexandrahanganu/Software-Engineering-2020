import java.awt.*;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

import javax.imageio.ImageIO;
import javax.swing.JButton;
import javax.swing.*;

public class MainFrame extends JFrame{


    public MainFrame()
    {
        super("My Drawing Application");
        init();
    }

    private void init()
    {
        JFrame frame = new JFrame("Flow Layout");
        JButton button,button1, button2;
        button = new JButton("CT");
        button1 = new JButton("Mask");
        button2 = new JButton("3D");
        frame.add(button);
        frame.add(button1);
        frame.add(button2);
        frame.setLayout(new FlowLayout());
        frame.setSize(300,300);
        frame.setVisible(true);
        button.addActionListener(this::save);
        button1.addActionListener(this::save);
        button2.addActionListener(this::save);
    }

    private void save(ActionEvent e) {
        try{
            String s= null;
            Process p = Runtime.getRuntime().exec("python C:\\Users\\Ioana\\PycharmProjects\\cod_mask\\code.py");
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while ((s = in.readLine()) != null) {
                System.out.println(s);
            }

        }
        catch(IOException ex){
            ex.printStackTrace();
        }
    }
}
