import 'package:flutter/material.dart';

class TajweedAudioPlayerScreen extends StatefulWidget {
  const TajweedAudioPlayerScreen({Key? key}) : super(key: key);

  @override
  _TajweedAudioPlayerScreenState createState() => _TajweedAudioPlayerScreenState();
}

class _TajweedAudioPlayerScreenState extends State<TajweedAudioPlayerScreen> {
  bool _isPlaying = false;
  double _sliderValue = 12.0; // Simulated current playback position in seconds
  final double _totalDuration = 45.0; // Simulated total recording time in seconds

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFFDFBF7), // Pearl White Base
      appBar: AppBar(
        backgroundColor: const Color(0xFF0F5132), // Emerald Green
        title: const Text(
          "Tajweed Audio Review",
          style: TextStyle(color: Color(0xFFD4AF37), fontWeight: FontWeight.bold, fontSize: 18),
        ),
        elevation: 0,
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              const SizedBox(height: 20),
              // 1. Surah Meta Card Display Box
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: Colors.grey.shade200),
                ),
                child: Column(
                  children: const [
                    Text(
                      "REVIEWING RECITATION",
                      style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Colors.grey, letterSpacing: 1.1),
                    ),
                    SizedBox(height: 8),
                    Text(
                      "Surah Al-Fatiha",
                      style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Color(0xFF0F5132)),
                    ),
                    SizedBox(height: 4),
                    Text(
                      "Ayah 1 - 7 (Submitted Audio)",
                      style: TextStyle(fontSize: 14, color: Colors.grey),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 40),

              // 2. Playback Audio Slider Seekbar Dock
              Column(
                children: [
                  Slider(
                    value: _sliderValue,
                    min: 0.0,
                    max: _totalDuration,
                    activeColor: const Color(0xFF0F5132),
                    inactiveColor: Colors.grey.shade200,
                    onChanged: (value) {
                      setState(() {
                        _sliderValue = value;
                      });
                    },
                  ),
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 20.0),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text("0:${_sliderValue.toInt().toString().padLeft(2, '0')}", style: const TextStyle(color: Colors.grey, fontSize: 12)),
                        Text("0:${_totalDuration.toInt()}", style: const TextStyle(color: Colors.grey, fontSize: 12)),
                      ],
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 24),

              // 3. Central Media Controller Control Buttons Dock
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  IconButton(
                    icon: const Icon(Icons.replay_10_rounded, size: 36, color: Color(0xFF0F5132)),
                    onPressed: () {
                      setState(() {
                        _sliderValue = (_sliderValue - 10).clamp(0.0, _totalDuration);
                      });
                    },
                  ),
                  const SizedBox(width: 24),
                  GestureDetector(
                    onTap: () {
                      setState(() {
                        _isPlaying = !_isPlaying;
                      });
                    },
                    child: Container(
                      padding: const EdgeInsets.all(18),
                      decoration: const BoxDecoration(color: Color(0xFF0F5132), shape: BoxShape.circle),
                      child: Icon(
                        _isPlaying ? Icons.pause_rounded : Icons.play_arrow_rounded,
                        size: 44,
                        color: const Color(0xFFD4AF37),
                      ),
                    ),
                  ),
                  const SizedBox(width: 24),
                  IconButton(
                    icon: const Icon(Icons.forward_10_rounded, size: 36, color: Color(0xFF0F5132)),
                    onPressed: () {
                      setState(() {
                        _sliderValue = (_sliderValue + 10).clamp(0.0, _totalDuration);
                      });
                    },
                  ),
                ],
              ),
              const SizedBox(height: 40),

              // 4. Mistake Timeline Shortcuts Section Heading
              const Align(
                alignment: Alignment.centerLeft,
                child: Text(
                  "Jump to Mistakes (Timestamps)",
                  style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Color(0xFF0F5132)),
                ),
              ),
              const SizedBox(height: 12),

              // 5. Clickable Waveform Audio Shortcut Navigation List
              Expanded(
                child: ListView(
                  children: [
                    _buildTimestampErrorItem(
                      timeLabel: "0:01 - 0:02",
                      errorContext: "Makhraj Error (الْحَمْدُ)",
                      onTap: () {
                        setState(() {
                          _sliderValue = 1.25; // Directly jump audio to mistake seconds
                          _isPlaying = true;
                        });
                      },
                    ),
                    const SizedBox(height: 10),
                    _buildTimestampErrorItem(
                      timeLabel: "0:12 - 0:14",
                      errorContext: "Madd Prolongation Error (الرَّحِيمِ)",
                      onTap: () {
                        setState(() {
                          _sliderValue = 12.0;
                          _isPlaying = true;
                        });
                      },
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildTimestampErrorItem({required String timeLabel, required String errorContext, required VoidCallback onTap}) {
    return Container(
      decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade100)),
      child: ListTile(
        onTap: onTap,
        leading: const Icon(Icons.audio_file_outlined, color: Colors.orange, size: 24),
        title: Text(errorContext, style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 13, color: Colors.black87)),
        subtitle: Text("Audio Position: $timeLabel seconds", style: const TextStyle(fontSize: 11, color: Colors.grey)),
        trailing: const Icon(Icons.play_circle_fill_rounded, color: Color(0xFF0F5132), size: 28),
      ),
    );
  }
}
