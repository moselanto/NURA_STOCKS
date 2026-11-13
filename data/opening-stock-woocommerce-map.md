# Opening stock -> WooCommerce mapping (draft, 13 Nov 2026)

Source for website products/colours: `nura-experience/data/wa-catalogue.php` in moselanto/nurabeauty.co.ke (WhatsApp catalogue of 2 Nov 2026 mapped to live product IDs; Catalogue sync made website colour options match it). The live store could not be reached from the build tools on 13 Nov, so every match must be checked in wp-admin before loading counts.

Match: **yes** = exact product and colour; **check** = likely, confirm; **no** = nothing on the website.

| SKU | Stock line | Website product (ID) | Website colour | Match |
|---|---|---|---|---|
| NURA-LWF-2 | Loose Wave Frontal, Black colour 2 | Loose Wave Frontal (364) | Black (only one black) | check |
| NURA-LWF-1 | Loose Wave Frontal, Black colour 1 | Loose Wave Frontal (364) | Black (only one black) | check |
| NURA-LWF-BUR | Loose Wave Frontal, Burgundy | Loose Wave Frontal (364) | Burgundy | yes |
| NURA-LWF-33 | Loose Wave Frontal, 33 | Loose Wave Frontal (364) | 33 | yes |
| NURA-LWF-RW | Loose Wave Frontal, Red Wine | Loose Wave Frontal (364) | Red wine | yes |
| NURA-LWF-2-30 | Loose Wave Frontal, 2/30 | Loose Wave Frontal (364) | none (site has 1/30, 1/27, 1/350) | no colour |
| NURA-LWF-30 | Loose Wave Frontal, 30 | Loose Wave Frontal (364) | 30 | yes |
| NURA-LW44-99J | Loose Wave 4x4, 99J | 4x4 Loose Wave Hair Closure (243) | C1 99J | check |
| NURA-LW44-1 | Loose Wave 4x4, Black colour 1 | 4x4 Loose Wave Hair Closure (243) | Black | yes |
| NURA-LW44-33 | Loose Wave 4x4, 33 | 4x4 Loose Wave Hair Closure (243) | C33 | yes |
| NURA-BSHF-613 | Bone Straight High Fibre, 613 | Luxury Fibre Bone Straight Frontal (274) | 613 | yes |
| NURA-BSHF-PD | Bone Straight High Fibre, Piano Dark | Luxury Fibre Bone Straight Frontal (274) | Dark Piano | yes |
| NURA-BSHF-BLK | Bone Straight High Fibre, Black | Luxury Fibre Bone Straight Frontal (274) | Black | yes |
| NURA-BW-PD | Body Wave, Piano Dark | Luxury Body Wave (377) | Piano (no "dark" option) | check |
| NURA-BW-613 | Body Wave, 613 | Luxury Body Wave (377) | 613 | yes |
| NURA-BW-BLK | Body Wave, Black | Luxury Body Wave (377) | Black | yes |
| NURA-BOBA-BLK/99J/33/30 | Bob Amanda (4 colours) | none (site has Bob Wig 271, Human Hair Bob 318, Bob Wavy 266, none with colours) | - | no product |
| NURA-EMP-1B, NURA-EMP-1-33 | Empress (2 colours) | none | - | no product |
| NURA-WF-BLK | Wonderful Frontal, Black | none | - | no product |
| NURA-NEG22-1-30 | 2x2 Negatron, 1/30 | none (2x2 Minky Closure Wig 386 has 1/30 but is a different wig) | - | no product |
