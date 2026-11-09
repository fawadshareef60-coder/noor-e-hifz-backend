import 'package:flutter/material.dart';
import 'screens/login_screen.dart';
import 'screens/dashboard_screen.dart';
import 'screens/report_screen.dart';
import 'screens/guardian_screen.dart';
import 'screens/leaderboard_screen.dart';

void main() {
  runApp(const NoorEHifzApp());
}

class NoorEHifzApp extends StatelessWidget {
  const NoorEHifzApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Noor-e-Hifz AI Madrasa',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primaryColor: const Color(0xFF0F5132), // Pure Emerald Green
        scaffoldBackgroundColor: const Color(0xFFFDFBF7), // Soft Pearl Cream Base
        fontFamily: 'Traditional Arabic',
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF0F5132),
          secondary: const Color(0xFFD4AF37), // Spiritual Accent Gold
        ),
      ),
      // App starting landing point set to Login Screen
      home: const LoginScreen(),
      routes: {
        '/login': (context) => const LoginScreen(),
        '/dashboard': (context) => const StudentDashboardScreen(),
        '/report': (context) => const AIReportScreen(),
        '/guardian': (context) => const GuardianDashboardScreen(),
        '/leaderboard': (context) => const HifzLeaderboardScreen(),
      },
    );
  }
}
