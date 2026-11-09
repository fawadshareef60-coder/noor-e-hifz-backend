import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  // Apne Render/HuggingFace ya gateway local URL ko dynamic handle karne ke liye variable
  static const String baseUrl = "http://localhost:8000/api/v1";

  // ==========================================
  // 1. STUDENT REGISTRATION API PIPELINE
  // ==========================================
  static Future<bool> registerStudent(String email, String password, String phoneNumber) async {
    final url = Uri.parse("$baseUrl/auth/register");
    try {
      final response = await http.post(
        url,
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({
          "email": email,
          "password": password,
          "phone_number": phoneNumber.isNotEmpty ? phoneNumber : null,
          "role": "student"
        }),
      );

      if (response.statusCode == 211 || response.statusCode == 200) {
        return true; // Successfully registered in database
      }
      return false;
    } catch (e) {
      print("Registration Service Error: $e");
      return false;
    }
  }

  // ==========================================
  // 2. STUDENT LOGIN / JWT KEY CAPTURE
  // ==========================================
  static Future<String?> loginStudent(String username, String password) async {
    final url = Uri.parse("$baseUrl/auth/login");
    try {
      // OAuth2 Standard Password request form standard formatting
      final response = await http.post(
        url,
        headers: {"Content-Type": "application/x-www-form-urlencoded"},
        body: {
          "username": username,
          "password": password,
        },
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        return data["access_token"]; // Secure active session JWT Key token
      }
      return null;
    } catch (e) {
      print("Login Service Error: $e");
      return null;
    }
  }

  // ==========================================
  // 3. FETCH QURAN MASTER SURAH CONTENT LIST
  // ==========================================
  static Future<List<dynamic>> fetchSurahList() async {
    final url = Uri.parse("$baseUrl/quran/surahs");
    try {
      final response = await http.get(url);
      if (response.statusCode == 200) {
        return jsonDecode(response.body); // Returns verified list from postgres
      }
      return [];
    } catch (e) {
      print("Quran Navigation Service Error: $e");
      return [];
    }
  }
}
