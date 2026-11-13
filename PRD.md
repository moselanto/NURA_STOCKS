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

## Open questions for the owner

1. Does the shop already turn on stock tracking ("Manage stock") for products in WooCommerce, and are the numbers there correct today? If not, Phase 1 starts with a full stock-take.
2. Is all stock kept in one place (the studio, Stanbank House) or also somewhere else?
3. Do WhatsApp orders become WooCommerce orders that should reduce stock, or are they only recorded when paid?
4. Who may adjust stock: only the owner, or shop managers too?
5. Care products: count them the same way as wigs (yes/no)?
6. Should a payment-plan reservation stay counted as "reserved" (shown separately) rather than simply removed from the shelf count?
