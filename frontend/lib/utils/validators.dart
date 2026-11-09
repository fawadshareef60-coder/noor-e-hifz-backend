class AppValidators {
  // ==========================================
  // 1. EMAIL FORMAT VALIDATION REGEX
  // ==========================================
  static String? validateEmail(String? value) {
    if (value == null || value.trim().isEmpty) {
      return "Email address likhna lazmi hai.";
    }
    
    // Regular Expression matching authentic secure email patterns
    final emailRegex = RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$');
    if (!emailRegex.hasMatch(value.trim())) {
      return "Ghalat format! Baraye meharbani sahi email address likhein.";
    }
    
    return null; // Passed verification successfully
  }

  // ==========================================
  // 2. PASSWORD SECURITY STRENGTH CHECK
  // ==========================================
  static String? validatePassword(String? value) {
    if (value == null || value.isEmpty) {
      return "Password likhna lazmi hai.";
    }
    
    // Backend schemas validation match checkpoint (Part 4 min_length=6 specification)
    if (value.length < 6) {
      return "Security alert: Password kam az kam 6 characters ka hona chahiye.";
    }
    
    return null;
  }

  // ==========================================
  // 3. PAKISTAN PHONE NUMBER FORMAT VALIDATOR
  // ==========================================
  static String? validatePhoneNumber(String? value) {
    if (value == null || value.trim().isEmpty) {
      return null; // Phone number optional hai, isliye khali chora ja sakta hai
    }
    
    final phoneRegex = RegExp(r'^((\+92)|(0092)|(0))?3\d{9}$');
    if (!phoneRegex.hasMatch(value.trim())) {
      return "Ghalat number! Baraye meharbani sahi Pakistani mobile number likhein.";
    }
    
    return null;
  }
}
