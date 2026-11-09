import 'package:flutter/material.dart';

class GuardianDashboardScreen extends StatelessWidget {
  const GuardianDashboardScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFFDFBF7), // Pearl White theme color
      appBar: AppBar(
        backgroundColor: const Color(0xFF0F5132), // Emerald Green
        title: const Text(
          "Parental Supervision Gateway",
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
              // 1. Linked Student Identity Information Profile Badge
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: Colors.grey.shade200),
                ),
                child: Row(
                  children: [
                    CircleAvatar(
                      radius: 24,
                      backgroundColor: const Color(0xFF0F5132).withOpacity(0.1),
                      child: const Icon(Icons.person, color: Color(0xFF0F0F5132)),
                    ),
                    const SizedBox(width: 16),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: const [
                        Text(
                          "Linked Student Profile",
                          style: TextStyle(fontSize: 12, color: Colors.grey),
                        ),
                        SizedBox(height: 4),
                        Text(
                          "Tehmina Urooj",
                          style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Color(0xFF0F5132)),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 24),

              // 2. Section Heading
              const Text(
                "Memorization Analytics Insights",
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Color(0xFF0F5132)),
              ),
              const SizedBox(height: 12),

              // 3. Dynamic Progress Performance Grid Cards
              Row(
                children: [
                  Expanded(
                    child: _buildMetricCard(
                      title: "Total Memorized",
                      value: "25 Ayahs",
                      icon: Icons.bookmark_added_rounded,
                    ),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    child: _buildMetricCard(
                      title: "Global Accuracy",
                      value: "94.50%",
                      icon: Icons.speed_rounded,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 28),

              // 4. Activity Logs Section Title
              const Text(
                "Recent Recitation Activities Timeline",
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Color(0xFF0F5132)),
              ),
              const SizedBox(height: 12),

              // 5. Scrollable Analytics Updates Logs Feed
              Expanded(
                child: ListView(
                  children: [
                    _buildActivityTimelineItem(
                      activityTitle: "Sabaq Audio Recitation Submitted",
                      timestamp: "Today at 04:15 PM",
                      details: "Surah Al-Fatiha (Ayah 1 - 7). Accuracy level rated high by system AI auditor.",
                      statusIcon: Icons.check_circle_rounded,
                      statusColor: Colors.green,
                    ),
                    const SizedBox(height: 14),
                    _buildActivityTimelineItem(
                      activityTitle: "Study Session Time Logged",
                      timestamp: "Yesterday",
                      details: "Spent 45 minutes practicing makhraj articulation correction pathways.",
                      statusIcon: Icons.access_time_filled_rounded,
                      statusColor: const Color(0xFFD4AF37),
                    ),
                  ],
                ),
              )
            ],
          ),
        ),
      ),
    );
  }

  // Custom Helper UI Component Widget for core numbers statistics box
  Widget _buildMetricCard({required String title, required String value, required IconData icon}) {
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
          Icon(icon, color: const Color(0xFFD4AF37), size: 28),
          const SizedBox(height: 14),
          Text(title, style: const TextStyle(fontSize: 12, color: Colors.grey, fontWeight: FontWeight.w500)),
          const SizedBox(height: 4),
          Text(value, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Color(0xFF0F5132))),
        ],
      ),
    );
  }

  // Custom Helper UI Component Widget for chronological timeline elements
  Widget _buildActivityTimelineItem({
    required String activityTitle,
    required String timestamp,
    required String details,
    required IconData statusIcon,
    required Color statusColor,
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
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(activityTitle, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 13, color: Colors.black87)),
              Icon(statusIcon, color: statusColor, size: 18),
            ],
          ),
          const SizedBox(height: 4),
          Text(timestamp, style: const TextStyle(fontSize: 11, color: Colors.grey)),
          const Divider(height: 20),
          Text(details, style: const TextStyle(fontSize: 12, color: Colors.black54, height: 1.3)),
        ],
      ),
    );
  }
}
