# NURA Stocks - plan (PRD)

Draft for owner approval, 13 Nov 2026. Nothing here is built yet.

## Goal

The owner and staff can open **NURA Desk > Stock** and see, at a glance and correctly, how many of each wig and care product are on the shelf, for every colour and length, and why each number changed.

## Where it lives

A new NURA Desk module in the `nura-experience` plugin (website repo), file `includes/class-nura-desk-stock.php`, class `NURAX_Desk_Stock`, with its own Desk tab **Stock**. The plan and specs live in this repo; the code is developed here under `nura-experience/` (same paths as the website repo) and copied into the website repo for each plugin release, so there is only ever one plugin zip to install.

## Phase 1 - live stock counts (first priority)

1. **Stock list**
   - One row per product, with its colours/lengths underneath (variations).
   - Columns: photo, name, option, SKU, on shelf, reserved for payment plans, available, status (in stock / low / out), last change.
   - Filters: category (wigs, care products...), status, search. Totals at the top: units on shelf, products out of stock, products low.
   - Products that do not yet track stock are listed separately with a "Start counting" action.
2. **Stock-take / opening count**
   - Enter the real counted quantity per product/option (one screen, or upload a spreadsheet).
   - Turns on WooCommerce stock tracking for those items and records the difference as a stock-take movement.
3. **Adjust stock**
   - Add or remove units with a required reason: received from supplier, damaged, returned by client, given away / used in studio, count correction.
   - "Received" can optionally link to a **Stock bought** entry in Accounts (no double entry of money).
4. **Movement history**
   - New table `nurax_stock_moves`: product, variation, change (+/-), before, after, reason, source (online order, till sale, WhatsApp order, payment plan, void/cancel/refund, adjustment, stock-take), order or plan reference, staff member, time, note.
   - Filled automatically from WooCommerce stock hooks (order stock reduce/restore, product and variation stock set) and from the Desk modules, so every change on the site is captured.
   - History per product and an Excel/CSV download.
5. **Permissions**
   - New staff permissions: "See stock" (default on) and "Adjust stock / stock-take" (default off for shop managers). New activity-log area `stock`.

## Phase 2 - later (not in Phase 1)

- Low-stock threshold per product and alerts (WhatsApp / e-mail).
- Stock value at buying price and a stock-take report that ties to Accounts.
- Supplier purchase records with quantities.
- Suggestions from Sourced sales ("worth stocking").

## Owner decisions (13 Nov 2026)

1. **Manage stock is already on** in WooCommerce and the owner says the counts there are correct. Phase 1 reads them as they are; the opening stock register (`data/`) is loaded only for lines that match a website product and colour.
2. **More than one location.** Some stock is kept away from the studio. Phase 1 adds locations: the WooCommerce count stays the total, and NURA Stocks splits it by location (table `nurax_stock_locations` + per-location quantities), with a "Move stock" action between locations (logged, total unchanged). Location names still needed from the owner.
3. **WhatsApp orders reduce stock.** Proposed: a WhatsApp order reserves the piece when it is placed and takes it off the shelf when it is paid; a cancelled or expired order releases the reservation.
4. **Shop managers can change stock** (adjust, receive, stock-take, move) as well as the owner. Every change needs a reason and is written to the activity log.
5. **Care products are counted** the same way as wigs.
6. **Payment-plan reservations show as "Reserved"** in their own column: On shelf - Reserved = Available to sell.

## Still needed from the owner

- Names of the stock locations, and which opening-stock lines are kept where.
- Decisions on the website mapping (`data/opening-stock-woocommerce-map.md`): Black colour 1 vs colour 2 on Loose Wave Frontal, 99J/burgundy on the 4x4 closure, Piano vs Piano Dark on Body Wave, colour 2/30, and new products for Bob Amanda, Empress, Wonderful Frontal and 2x2 Negatron.
