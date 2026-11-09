import 'package:flutter/material.dart';
import 'api_service.dart';

class AuthProvider extends ChangeNotifier {
  String? _authToken;
  bool _isLoading = false;
  String? _currentUserId;
  String? _userRole;

  // Getters to read secure private state across app framework screens
  String? get token => _authToken;
  bool get isLoading => _isLoading;
  bool get isAuthenticated => _authToken != null;
  String? get currentUserId => _currentUserId;
  String? get userRole => _userRole;

  // ==========================================
  // 1. EXECUTE LOGGED IN USER SESSION STATE
  // ==========================================
  Future<bool> executeLogin(String email, String password) async {
    _isLoading = true;
    notifyListeners(); // Refresh screens loader animation layout state

    try {
      final tokenResult = await ApiService.loginStudent(email, password);
      
      if (tokenResult != null) {
        _authToken = tokenResult;
        // Temporary test allocation values matching manual Supabase tables insert row values
        _currentUserId = "886e3d86-test-uuid-student"; 
        _userRole = "student";
        
        _isLoading = false;
        notifyListeners(); // Successfully state refresh trigger across active screens
        return true;
      }
    } catch (e) {
      print("Auth Provider Session Trigger Error: $e");
    }

    _isLoading = false;
    notifyListeners();
    return false;
  }

  // ==========================================
  // 2. CLEAR SESSION LOGOUT PIPELINE
  // ==========================================
  void executeLogout() {
    _authToken = null;
    _currentUserId = null;
    _userRole = null;
    notifyListeners(); // Returns interface state back to clean LoginScreen landing map
  }
}
