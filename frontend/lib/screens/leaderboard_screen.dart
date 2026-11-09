import 'package:flutter/material.dart';

class HifzLeaderboardScreen extends StatelessWidget {
  const HifzLeaderboardScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFFDFBF7), // Pearl White Base
      appBar: AppBar(
        backgroundColor: const Color(0xFF0F5132), // Emerald Green
        title: const Text(
          "Madrasa Competition Board",
          style: TextStyle(color: Color(0xFFD4AF37), fontWeight: FontWeight.bold, fontSize: 18),
        ),
        elevation: 0,
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // 1. Current Student Rank Status Summary Overview Card
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: const Color(0xFF0F5132),
                  borderRadius: BorderRadius.circular(16),
                  boxShadow: [
                    BoxShadow(color: const Color(0xFF0F5132).withOpacity(0.2), spreadRadius: 2, blurRadius: 10)
                  ]
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Row(
                      children: [
                        const Icon(Icons.emoji_events_rounded, color: Color(0xFFD4AF37), size: 44),
                        const SizedBox(width: 14),
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: const [
                            Text("YOUR CURRENT RANK", style: TextStyle(color: Color(0xFFD4AF37), fontSize: 11, fontWeight: FontWeight.bold, letterSpacing: 1.1)),
                            SizedBox(height: 4),
                            Text("4th Position", style: TextStyle(color: Colors.white, fontSize: 20, fontWeight: FontWeight.bold)),
                          ],
                        ),
                      ],
                    ),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.end,
                      children: const [
                        Text("TOTAL STARS", style: TextStyle(color: Colors.grey, fontSize: 10, fontWeight: FontWeight.bold)),
                        SizedBox(height: 4),
                        Text("⭐ 480", style: TextStyle(color: Color(0xFFD4AF37), fontSize: 18, fontWeight: FontWeight.bold)),
                      ],
                    )
                  ],
                ),
              ),
              const SizedBox(height: 24),

              // 2. Interactive Earned Spiritual Badges Segment
              const Text("Your Achieved Badges", style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Color(0xFF0F5132))),
              const SizedBox(height: 12),
              SizedBox(
                height: 85,
                child: ListView(
                  scrollDirection: Axis.horizontal,
                  children: [
                    _buildBadgeItem("Tajweed Star", Icons.g_translate_rounded, Colors.green),
                    const SizedBox(width: 14),
                    _buildBadgeItem("7-Day Streak", Icons.local_fire_department_rounded, Colors.orange),
                    const SizedBox(width: 14),
                    _buildBadgeItem("Juz 1 Done", Icons.auto_stories_rounded, Colors.purple),
                    const SizedBox(width: 14),
                    _buildBadgeItem("Perfect Sabqi", Icons.verified_rounded, Colors.blue),
                  ],
                ),
              ),
              const SizedBox(height: 24),

              // 3. Global Top Students Rankings List Title
              const Text("Top Reciters This Week", style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Color(0xFF0F5132))),
              const SizedBox(height: 12),

              // 4. Scrollable Rankings List Sheet
              Expanded(
                child: ListView(
                  children: [
                    _buildRankStudentItem(rank: "1", name: "Ahmed Ali", accuracy: "98.80%", stars: "620", isTop: true),
                    const SizedBox(height: 12),
                    _buildRankStudentItem(rank: "2", name: "Fatima Khan", accuracy: "97.40%", stars: "580", isTop: true),
                    const SizedBox(height: 12),
                    _buildRankStudentItem(rank: "3", name: "Zainab Bibi", accuracy: "95.90%", stars: "510", isTop: true),
                    const SizedBox(height: 12),
                    _buildRankStudentItem(rank: "4", name: "Tehmina Urooj (You)", accuracy: "94.50%", stars: "480", isTop: false),
                  ],
                ),
              )
            ],
          ),
        ),
      ),
    );
  }

  // Custom internal widget to create badge indicators easily
  Widget _buildBadgeItem(String title, IconData icon, Color baseColor) {
    return Container(
      width: 90,
      padding: const EdgeInsets.all(10),
      decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(12), border: Border.all(color: Colors.grey.shade200)),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(icon, color: baseColor, size: 28),
          const SizedBox(height: 6),
          Text(title, maxLines: 1, overflow: TextOverflow.ellipsis, style: const TextStyle(fontSize: 11, fontWeight: FontWeight.w600, color: Colors.black87)),
        ],
      ),
    );
  }

  // Custom row component widget for student list profiles entries
  Widget _buildRankStudentItem({required String rank, required String name, required String accuracy, required String stars, required bool isTop}) {
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: isTop ? const Color(0xFFD4AF37).withOpacity(0.4) : Colors.grey.shade100),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Row(
            children: [
              Container(
                width: 32,
                height: 32,
                decoration: BoxDecoration(color: isTop ? const Color(0xFFD4AF37).withOpacity(0.2) : Colors.grey.shade100, shape: BoxShape.circle),
                child: Center(child: Text(rank, style: TextStyle(fontWeight: FontWeight.bold, color: isTop ? const Color(0xFF0F5132) : Colors.grey))),
              ),
              const SizedBox(width: 16),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(name, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14, color: isTop ? const Color(0xFF0F5132) : Colors.black87)),
                  const SizedBox(height: 2),
                  Text("Accuracy: $accuracy", style: const TextStyle(fontSize: 12, color: Colors.grey)),
                ],
              )
            ],
          ),
          Text("⭐ $stars", style: const TextStyle(fontWeight: FontWeight.bold, color: Color(0xFFD4AF37), fontSize: 14)),
        ],
      ),
    );
  }
}
