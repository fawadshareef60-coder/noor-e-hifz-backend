import 'package:flutter/material.dart';

class AIReportScreen extends StatelessWidget {
  const AIReportScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFFDFBF7), // Pearl White Base
      appBar: AppBar(
        backgroundColor: const Color(0xFF0F5132), // Emerald Green
        title: const Text(
          "AI Recitation Audit Report",
          style: TextStyle(color: Color(0xFFD4AF37), fontWeight: FontWeight.bold),
        ),
        elevation: 0,
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // 1. Overall Accuracy Percentage Ring Banner
              Center(
                child: Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(24),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(color: Colors.grey.shade200),
                  ),
                  child: Column(
                    children: [
                      const Text(
                        "MUTABIQAT ACCURACY SCORE",
                        style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.grey, letterSpacing: 1.2),
                      ),
                      const SizedBox(height: 16),
                      Stack(
                        alignment: Alignment.center,
                        children: [
                          SizedBox(
                            width: 100,
                            height: 100,
                            child: CircularProgressIndicator(
                              value: 0.945, // 94.5% Score
                              strokeWidth: 10,
                              valueColor: const AlwaysStoppedAnimation<Color>(Color(0xFF0F5132)),
                              backgroundColor: Colors.grey.shade100,
                            ),
                          ),
                          const Text(
                            "94.5%",
                            style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Color(0xFF0F5132)),
                          )
                        ],
                      ),
                      const SizedBox(height: 16),
                      const Text(
                        "MashaAllah! Boht Umdah Tilawat",
                        style: TextStyle(fontSize: 16, fontWeight: FontWeight.w600, color: Color(0xFF0F5132)),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 28),

              // 2. Section Heading
              const Text(
                "Detected Mistake Logs (Ghaltiyan)",
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Color(0xFF0F5132)),
              ),
              const SizedBox(height: 12),

              // 3. Detailed Fault Cards List
              Expanded(
                child: ListView(
                  children: [
                    // Mistake 1: Pronunciation Makhraj Error
                    _buildMistakeCard(
                      ayahText: "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
                      errorType: "Pronunciation (Makhraj)",
                      wordIndex: "Word 1 (الْحَمْدُ)",
                      correction: "Haa (ح) ki jagah Ha (ه) parha gaya. Makhraj se ada karein.",
                      severityColor: Colors.orange,
                    ),
                    const SizedBox(height: 14),
                    
                    // Mistake 2: Tajweed Madd/Ghunnah Error
                    _buildMistakeCard(
                      ayahText: "الرَّحْمَٰنِ الرَّحِيمِ",
                      errorType: "Tajweed Rules",
                      wordIndex: "Word 2 (الرَّحِيمِ)",
                      correction: "Madd-Arid-Lis-Sukoon ki prolongation kam thi. 2-4 harakat tak khenchein.",
                      severityColor: Colors.blue,
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 16),

              // 4. Automated Revision Trigger System Notification Card
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: const Color(0xFFD4AF37).withOpacity(0.12),
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: const Color(0xFFD4AF37), width: 0.8),
                ),
                child: Row(
                  children: [
                    const Icon(Icons.auto_graph_rounded, color: Color(0xFF0F5132), size: 28),
                    const SizedBox(width: 14),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: const [
                          Text(
                            "AI Smart Revision Plan Updated",
                            style: TextStyle(fontWeight: FontWeight.bold, color: Color(0xFF0F5132), fontSize: 14),
                          ),
                          SizedBox(height: 4),
                          Text(
                            "Yeh Ayahs aapke kal ke Sabqi revision schedule mein shamil kar di gayi hain.",
                            style: TextStyle(color: Colors.black87, fontSize: 12),
                          ),
                        ],
                      ),
                    )
                  ],
                ),
              )
            ],
          ),
        ),
      ),
    );
  }

  // Helper Custom Widget to render granular error cards dynamically
  Widget _buildMistakeCard({
    required String ayahText,
    required String errorType,
    required String wordIndex,
    required String correction,
    required Color severityColor,
  }) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: Colors.grey.shade200),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            ayahText,
            style: const TextStyle(fontSize: 20, fontFamily: 'Traditional Arabic', fontWeight: FontWeight.bold, height: 1.5),
          ),
          const Divider(height: 24),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(color: severityColor.withOpacity(0.15), borderRadius: BorderRadius.circular(6)),
                child: Text(errorType, style: TextStyle(color: severityColor, fontWeight: FontWeight.bold, fontSize: 11)),
              ),
              Text(wordIndex, style: const TextStyle(color: Colors.grey, fontSize: 12, fontWeight: FontWeight.w500)),
            ],
          ),
          const SizedBox(height: 10),
          Text(
            "Correction: $correction",
            style: const TextStyle(fontSize: 13, color: Colors.black87, height: 1.3),
          ),
        ],
      ),
    );
  }
}
