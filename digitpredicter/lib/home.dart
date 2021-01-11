import 'package:flutter/material.dart';
import 'screens/drawpage.dart';
import 'screens/uploadimage.dart';
import 'package:digitpredicter/utilities/constants.dart';

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  int currentIndex = 0;

  @override
  Widget build(BuildContext context) {
    List tabs = [
      UploadImage(),
      DrawPage(),
    ];

    return Scaffold(
      appBar: AppBar(
        title: Text("MNIST Digit Recognizer"),
        backgroundColor: Colors.green[400],
      ),
      body: tabs[currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: currentIndex,
        iconSize: iconSize,
        selectedFontSize: selectedFontSize,
        unselectedFontSize: unselectedFontSize,
        selectedItemColor: Colors.green[400],
        unselectedItemColor: Colors.grey[400],
        items: [
          BottomNavigationBarItem(icon: Icon(Icons.image), label: "Image"),
          BottomNavigationBarItem(
              icon: Icon(Icons.bubble_chart), label: "Draw"),
        ],
        onTap: (index) {
          setState(() {
            currentIndex = index;
          });
        },
      ),
    );
  }
}
