# Opening stock - 13 Nov 2026 (register v4.0)

Source: owner's stock book and delivery list of 13 Nov 2026. Costs: actual cost of making each product line (bundles, ventilation, wig cap, labour), given by the owner on 13 Nov 2026; weighted average cost per piece. Only the pieces delivered on 13 Nov are on the shelf.

- Formatted register: `NURA-Beauty-Opening-Stock-Register-2026-11-13.xlsx` (v4.0; rebuild with `python scripts/build_opening_stock_register.py`)
- Machine-readable: `opening-stock-2026-11-13.csv`

| | Pieces | Value at cost (KES) |
|---|---|---|
| On the shelf (received 13 Nov) | **26** | **47,910.49** |
| Awaiting the vendor | **17** | 37,264.51 |
| Total in the stock book | **43** | 85,175.00 |

## Cost of making by product line (owner, 13 Nov 2026)

| Product line | Cost parts (KES) | Line total (KES) | Pieces in stock book | Average cost per piece (KES) |
|---|---|---|---|---|
| Loose Wave Frontal | Main batch 26,100 + Extra bundles 1,210 + Colour 30 (additional) 3,210 + Another frontal (additional) 2,300 | 32,820 | 17 | 1,930.59 |
| Loose Wave 4x4 Closure | Main batch 9,615 | 9,615 | 6 | 1,602.50 |
| Bone Straight High Fibre | Main batch 11,800 + Additional 3,100 | 14,900 | 6 | 2,483.33 |
| Body Wave | Main batch 14,700 | 14,700 | 6 | 2,450.00 |
| Bob Amanda | Main batch 7,340 | 7,340 | 4 | 1,835.00 |
| Empress | Main batch 4,100 | 4,100 | 2 | 2,050.00 |
| Wonderful Frontal (new trial) | Additional 1,000 | 1,000 | 1 | 1,000.00 |
| 2x2 Negatron Closure (new trial) | Additional 700 | 700 | 1 | 700.00 |
| **Total** | | **85,175** | **43** | |

Owner's written totals: main batch KES 75,065 and grand total KES 85,375. The listed line amounts add up to KES 74,865 and KES 85,175 (KES 200 less). The register uses the line amounts until the owner says which line carries the extra KES 200.

The 43 includes 1 over-delivered piece (Loose Wave Frontal colour 33: ordered 3, received 4). Pieces awaiting the vendor are not on the shelf and are not in the shelf stock value.

| SKU | Product | Colour | Ordered | On shelf | Awaiting vendor | Unit cost (KES) | Value on shelf (KES) | Status |
|---|---|---|---|---|---|---|---|---|
| NURA-LWF-2 | Loose Wave Frontal | Black (colour 2) | 3 | 3 | 0 | 1,930.59 | 5,791.76 | Received in full |
| NURA-LWF-1 | Loose Wave Frontal | Black (colour 1) | 2 | 2 | 0 | 1,930.59 | 3,861.18 | Received in full |
| NURA-LWF-BUR | Loose Wave Frontal | Burgundy | 3 | 2 | 1 | 1,930.59 | 3,861.18 | Part-received |
| NURA-LWF-33 | Loose Wave Frontal | Colour 33 | 3 | 4 | 0 | 1,930.59 | 7,722.35 | Over-delivered |
| NURA-LWF-RW | Loose Wave Frontal | Red Wine | 2 | 2 | 0 | 1,930.59 | 3,861.18 | Received in full |
| NURA-LWF-2-30 | Loose Wave Frontal | Colour 2/30 | 1 | 1 | 0 | 1,930.59 | 1,930.59 | Received in full |
| NURA-LWF-30 | Loose Wave Frontal | Colour 30 | 2 | 1 | 1 | 1,930.59 | 1,930.59 | Part-received |
| NURA-LW44-99J | Loose Wave 4x4 Closure | Colour 99J | 2 | 2 | 0 | 1,602.50 | 3,205.00 | Received in full |
| NURA-LW44-1 | Loose Wave 4x4 Closure | Black (colour 1) | 2 | 2 | 0 | 1,602.50 | 3,205.00 | Received in full |
| NURA-LW44-33 | Loose Wave 4x4 Closure | Colour 33 | 2 | 2 | 0 | 1,602.50 | 3,205.00 | Received in full |
| NURA-BSHF-613 | Bone Straight High Fibre | Colour 613 (blonde) | 2 | 0 | 2 | 2,483.33 | 0.00 | Awaiting delivery |
| NURA-BSHF-PD | Bone Straight High Fibre | Piano Dark | 2 | 0 | 2 | 2,483.33 | 0.00 | Awaiting delivery |
| NURA-BSHF-BLK | Bone Straight High Fibre | Black | 2 | 2 | 0 | 2,483.33 | 4,966.67 | Received in full |
| NURA-BW-PD | Body Wave | Piano Dark | 2 | 0 | 2 | 2,450.00 | 0.00 | Awaiting delivery |
| NURA-BW-613 | Body Wave | Colour 613 (blonde) | 2 | 0 | 2 | 2,450.00 | 0.00 | Awaiting delivery |
| NURA-BW-BLK | Body Wave | Black | 2 | 0 | 2 | 2,450.00 | 0.00 | Awaiting delivery |
| NURA-BOBA-BLK | Bob Amanda | Black | 1 | 1 | 0 | 1,835.00 | 1,835.00 | Received in full |
| NURA-BOBA-99J | Bob Amanda | Colour 99J | 1 | 0 | 1 | 1,835.00 | 0.00 | Awaiting delivery |
| NURA-BOBA-33 | Bob Amanda | Colour 33 | 1 | 1 | 0 | 1,835.00 | 1,835.00 | Received in full |
| NURA-BOBA-30 | Bob Amanda | Colour 30 | 1 | 0 | 1 | 1,835.00 | 0.00 | Awaiting delivery |
| NURA-EMP-1B | Empress | Colour 1B | 1 | 0 | 1 | 2,050.00 | 0.00 | Awaiting delivery |
| NURA-EMP-1-33 | Empress | Colour 1/33 | 1 | 0 | 1 | 2,050.00 | 0.00 | Awaiting delivery |
| NURA-WF-BLK | Wonderful Frontal (new trial) | Black | 1 | 0 | 1 | 1,000.00 | 0.00 | Awaiting delivery |
| NURA-NEG22-1-30 | 2x2 Negatron Closure (new trial) | Colour 1/30 | 1 | 1 | 0 | 700.00 | 700.00 | Received in full |
| **Total** | | | **42** | **26** | **17** | | **47,910.49** | |
