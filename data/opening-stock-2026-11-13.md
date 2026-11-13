# Opening stock - 13 Nov 2026 (register v4.1)

Source: owner's stock book and delivery list of 13 Nov 2026. Costs: actual cost of making each product line (bundles, ventilation, wig cap, labour) plus KES 200 transport for the wig maker to collect materials, given by the owner on 13-14 Nov 2026; weighted average cost per piece. Only the pieces delivered on 13 Nov are on the shelf.

- Formatted register: `NURA-Beauty-Opening-Stock-Register-2026-11-13.xlsx` (v4.1; rebuild with `python scripts/build_opening_stock_register.py`)
- Machine-readable: `opening-stock-2026-11-13.csv`

| | Pieces | Value at cost (KES) |
|---|---|---|
| On the shelf (received 13 Nov) | **26** | **48,020.87** |
| Awaiting the vendor | **17** | 37,354.13 |
| Total in the stock book | **43** | 85,375.00 |

## Cost of making by product line (owner, 13-14 Nov 2026)

| Product line | Cost parts (KES) | Line total (KES) | Pieces in stock book | Average cost per piece (KES) |
|---|---|---|---|---|
| Loose Wave Frontal | Main batch 26,100.00 + Extra bundles 1,210.00 + Colour 30 (additional) 3,210.00 + Another frontal (additional) 2,300.00 + Transport share 72.96 | 32,892.96 | 17 | 1,934.88 |
| Loose Wave 4x4 Closure | Main batch 9,615.00 + Transport share 25.69 | 9,640.69 | 6 | 1,606.78 |
| Bone Straight High Fibre | Main batch 11,800.00 + Additional 3,100.00 + Transport share 31.52 | 14,931.52 | 6 | 2,488.59 |
| Body Wave | Main batch 14,700.00 + Transport share 39.27 | 14,739.27 | 6 | 2,456.55 |
| Bob Amanda | Main batch 7,340.00 + Transport share 19.61 | 7,359.61 | 4 | 1,839.90 |
| Empress | Main batch 4,100.00 + Transport share 10.95 | 4,110.95 | 2 | 2,055.47 |
| Wonderful Frontal (new trial) | Additional 1,000.00 | 1,000.00 | 1 | 1,000.00 |
| 2x2 Negatron Closure (new trial) | Additional 700.00 | 700.00 | 1 | 700.00 |
| **Total** | | **85,375.00** | **43** | |

The KES 200 transport (wig maker collecting materials) is a shared cost of the main batch (owner's main-batch total KES 75,065). It is spread over the main-batch lines in proportion to their cost. Grand total KES 85,375 matches the owner's figure.

Open: the owner has not yet said which single wig carries each of the colour 30 cost (3,210), the other Loose Wave Frontal (2,300) and the Bone Straight extra (3,100); until then they are averaged across their product line.

The 43 includes 1 over-delivered piece (Loose Wave Frontal colour 33: ordered 3, received 4).

| SKU | Product | Colour | Ordered | On shelf | Awaiting vendor | Unit cost (KES) | Value on shelf (KES) | Status |
|---|---|---|---|---|---|---|---|---|
| NURA-LWF-2 | Loose Wave Frontal | Black (colour 2) | 3 | 3 | 0 | 1,934.88 | 5,804.64 | Received in full |
| NURA-LWF-1 | Loose Wave Frontal | Black (colour 1) | 2 | 2 | 0 | 1,934.88 | 3,869.76 | Received in full |
| NURA-LWF-BUR | Loose Wave Frontal | Burgundy | 3 | 2 | 1 | 1,934.88 | 3,869.76 | Part-received |
| NURA-LWF-33 | Loose Wave Frontal | Colour 33 | 3 | 4 | 0 | 1,934.88 | 7,739.52 | Over-delivered |
| NURA-LWF-RW | Loose Wave Frontal | Red Wine | 2 | 2 | 0 | 1,934.88 | 3,869.76 | Received in full |
| NURA-LWF-2-30 | Loose Wave Frontal | Colour 2/30 | 1 | 1 | 0 | 1,934.88 | 1,934.88 | Received in full |
| NURA-LWF-30 | Loose Wave Frontal | Colour 30 | 2 | 1 | 1 | 1,934.88 | 1,934.88 | Part-received |
| NURA-LW44-99J | Loose Wave 4x4 Closure | Colour 99J | 2 | 2 | 0 | 1,606.78 | 3,213.56 | Received in full |
| NURA-LW44-1 | Loose Wave 4x4 Closure | Black (colour 1) | 2 | 2 | 0 | 1,606.78 | 3,213.56 | Received in full |
| NURA-LW44-33 | Loose Wave 4x4 Closure | Colour 33 | 2 | 2 | 0 | 1,606.78 | 3,213.56 | Received in full |
| NURA-BSHF-613 | Bone Straight High Fibre | Colour 613 (blonde) | 2 | 0 | 2 | 2,488.59 | 0.00 | Awaiting delivery |
| NURA-BSHF-PD | Bone Straight High Fibre | Piano Dark | 2 | 0 | 2 | 2,488.59 | 0.00 | Awaiting delivery |
| NURA-BSHF-BLK | Bone Straight High Fibre | Black | 2 | 2 | 0 | 2,488.59 | 4,977.17 | Received in full |
| NURA-BW-PD | Body Wave | Piano Dark | 2 | 0 | 2 | 2,456.55 | 0.00 | Awaiting delivery |
| NURA-BW-613 | Body Wave | Colour 613 (blonde) | 2 | 0 | 2 | 2,456.55 | 0.00 | Awaiting delivery |
| NURA-BW-BLK | Body Wave | Black | 2 | 0 | 2 | 2,456.55 | 0.00 | Awaiting delivery |
| NURA-BOBA-BLK | Bob Amanda | Black | 1 | 1 | 0 | 1,839.90 | 1,839.90 | Received in full |
| NURA-BOBA-99J | Bob Amanda | Colour 99J | 1 | 0 | 1 | 1,839.90 | 0.00 | Awaiting delivery |
| NURA-BOBA-33 | Bob Amanda | Colour 33 | 1 | 1 | 0 | 1,839.90 | 1,839.90 | Received in full |
| NURA-BOBA-30 | Bob Amanda | Colour 30 | 1 | 0 | 1 | 1,839.90 | 0.00 | Awaiting delivery |
| NURA-EMP-1B | Empress | Colour 1B | 1 | 0 | 1 | 2,055.47 | 0.00 | Awaiting delivery |
| NURA-EMP-1-33 | Empress | Colour 1/33 | 1 | 0 | 1 | 2,055.47 | 0.00 | Awaiting delivery |
| NURA-WF-BLK | Wonderful Frontal (new trial) | Black | 1 | 0 | 1 | 1,000.00 | 0.00 | Awaiting delivery |
| NURA-NEG22-1-30 | 2x2 Negatron Closure (new trial) | Colour 1/30 | 1 | 1 | 0 | 700.00 | 700.00 | Received in full |
| **Total** | | | **42** | **26** | **17** | | **48,020.87** | |
