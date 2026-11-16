# HANDOVER - NURA Stocks (read this first)

Last updated: 14 Nov 2026, 00:35 EAT, by Town assistant (Ray). Next agent: read this file, then `PRD.md`, then `AGENTS.md`, then the website repo's `AGENTS.md`, `PROJECT-STATUS.md` and `HANDOVER.md` ([moselanto/nurabeauty.co.ke](https://github.com/moselanto/nurabeauty.co.ke)).

## 1. What this project is

Stock control for NURA Beauty (https://nurabeauty.co.ke): a **Stock** tab inside NURA Desk (the back office in the website's `nura-experience` plugin). Code is developed in this repo under the same paths as the website repo (`nura-experience/includes/...`) and copied into the website repo for each plugin release (one plugin zip; owner installs via Plugins > Upload > "Replace current with uploaded", then LiteSpeed Cache > Purge All).

Website live versions at hand-over: theme 1.134.0, plugin `nura-experience` 1.109.3.

## 2. Status at a glance

| Item | Status |
|---|---|
| Plan (`PRD.md`) and rules (`AGENTS.md`) | Done, owner decisions recorded |
| Opening stock count (13 Nov 2026) | Done, confirmed by owner |
| Opening stock register XLSX | Done, **v4.1** (`data/`) - actual making costs + transport, total KES 85,375 |
| Opening stock CSV + notes | Done, match v4.1 |
| Stock lines -> website products mapping | Draft (`data/opening-stock-woocommerce-map.md`), 6 lines unmatched |
| **NURA Desk Stock tab (code)** | **Released: plugin 1.110.0 installed live and tested by the owner 14 Nov (website order, till sale, WhatsApp order all correct under Stock). Copied to moselanto/nurabeauty.co.ke main in 5f0e709.** From now on the website repo is the source of truth for plugin code; the copies under `nura-experience/` here are a snapshot of 1.110.0. |

## 3. Stock figures (source of truth: `data/opening-stock-2026-11-13.csv`)

| | Pieces | Value at cost (KES) |
|---|---|---|
| On the shelf (delivery received 13 Nov) | **26** | **48,020.87** |
| Awaiting the vendor | **17** | 37,354.13 |
| Total in the owner's stock book | **43** | 85,375.00 |

- Only the 26 pieces delivered on 13 Nov are on the shelf (owner, 13 Nov). Nothing else is in stock.
- Stock book quantities = what was ordered from the vendor. Ordered total 42; Loose Wave Frontal colour 33 was ordered 3 and received 4 (1 over-delivered), so the book total is 43.
- Awaiting vendor (17): Body Wave 6 (Piano Dark 2, 613 2, Black 2); Bone Straight High Fibre 4 (613 2, Piano Dark 2); Loose Wave Frontal 2 (Burgundy 1, colour 30 1); Bob Amanda 2 (99J 1, 30 1); Empress 2 (1B 1, 1/33 1); Wonderful Frontal 1 (Black).
- Delivery list wording: the 4x4 closure "burgundy x 2" = the stock book's "99J x 2" (treated as the same 2 pieces).
- Costs (owner, 13-14 Nov; replace the earlier per-piece buying prices): every wig is made from scratch (bundles, ventilation, wig cap, labour). The KES 200 that was missing from the line amounts is transport for the wig maker to collect materials. It is a shared main-batch cost, spread over the main-batch lines in proportion to cost. Line totals: Loose Wave Frontal 32,892.96; Loose Wave 4x4 Closure 9,640.69; Bone Straight High Fibre 14,931.52; Body Wave 14,739.27; Bob Amanda 7,359.61; Empress 4,110.95; Wonderful Frontal (new trial) 1,000.00; 2x2 Negatron Closure (new trial) 700.00 = KES 85,375.00. Unit cost = weighted average per piece (line total / pieces in stock book): Loose Wave Frontal 1,934.88; Loose Wave 4x4 Closure 1,606.78; Bone Straight High Fibre 2,488.59; Body Wave 2,456.55; Bob Amanda 1,839.90; Empress 2,055.47; Wonderful Frontal 1,000.00; 2x2 Negatron Closure 700.00. These are the plugin's opening buying prices (`_nura_cost`). Owner decision 14 Nov: the extra 3,210 (LWF colour 30), 2,300 (another LWF) and 3,100 (Bone Straight) are full wig making costs and stay averaged across their line - do not assign them to single pieces.
- SKU format: `NURA-<line>-<colour>` (e.g. `NURA-LWF-33`); `/` in a colour code becomes `-`.

## 4. Files in this repo

| Path | What |
|---|---|
| `README.md` | Overview and what already exists in the website |
| `PRD.md` | Plan, phases, owner decisions |
| `AGENTS.md` | Rules for agents/developers |
| `HANDOVER.md` | This file |
| `data/NURA-Beauty-Opening-Stock-Register-2026-11-13.xlsx` | Register v4.1: Summary, Dashboard (pie, doughnut, bar, stacked column), Stock Register, Goods Received, Supplier Variances, Notes |
| `data/opening-stock-2026-11-13.csv` | Machine-readable stock lines (use this for loading counts) |
| `data/opening-stock-2026-11-13.md` | Human-readable table and totals |
| `data/opening-stock-woocommerce-map.md` | Draft line -> WooCommerce product/colour map |
| `scripts/build_opening_stock_register.py` | Rebuilds the XLSX (XlsxWriter + Pillow). Writes cached formula values so phone previews show figures. Edit `ITEMS`, `LINES`, `DELIVERY` at the top to change data |
| `assets/NURA_Beauty_Compact_Logo_Flat_Full_Colour_3000px.png` | Official logo (gold on transparent) |

Spreadsheet conventions the owner asked for: "very professional, international standards", NURA logo, black/gold brand (#0E0E0E, #C9972C), ISO 8601 dates, KES (ISO 4217), PCS, IAS 2 valuation note, charts. The logo must sit in its own header block with nothing beside or under it (owner reported overlaps twice; fixed in v2.2 by giving it dedicated rows sized for 20 px default rows). Save each new version under a new file name (owner's computer opened a cached old copy once).

## 5. Owner decisions (13 Nov 2026)

1. WooCommerce "Manage stock" is on; owner says website counts are correct.
2. Stock is kept in more than one place. **Owner names the places himself in NURA Desk Settings** (build a settings list of locations; no names are known yet).
3. **WhatsApp orders: reserve the piece when the order is placed; take it off the shelf when paid; release it if cancelled.**
4. Shop managers may change stock (adjust, receive, stock-take, move) as well as the owner; every change needs a reason and is logged.
5. Care products are counted the same way as wigs.
8. (14 Nov) Nothing goes out of stock by itself; customers can order any quantity; only staff Stop selling shows Out of stock.
6. Payment-plan stock shows as **Reserved** in its own column. Available = On shelf - Reserved.
7. **Leave the 6 unmatched lines unloaded until the owner decides** (see section 7).

## 6. Build notes for the Stock tab (what the code already does - verified in the website repo 13 Nov)

- **Plugin entry:** `nura-experience/nura-experience.php` requires each `includes/class-*.php` and boots in `nurax_init()`; version in header + `NURAX_VERSION`.
- **Desk menu/tabs:** `NURAX_Desk` (`class-nura-desk.php`): `CAP = 'manage_woocommerce'`, `MENU = 'nurax-desk'`; submenus added in `menu()` via `add_submenu_page( self::MENU, ... )`; the tab bar in `NURAX_Desk::header()` is a **hard-coded array** - add a `'nurax-stock' => 'Stock'` entry (or a filter) there. Helpers: `guard( $action )` (cap + nonce), `url()`, `kpi()`, `badge()`, `money()`, `export_btns()`, `csv_cell()`. Desk settings: `settings_page()` / `save_settings()` (option `nurax_desk`, `field_check()`).
- **Staff permissions:** `NURAX_Staff` (`class-nura-staff.php`): `defaults()` / `labels()` hold permission keys (add e.g. `stock_adjust`, default on per decision 4); `areas()` holds log areas (add `'stock' => 'Stock'`); `NURAX_Staff::can()`, `NURAX_Staff::log( $area, $summary, $o )`.
- **Till (POS):** `class-nura-desk-pos.php`; sales are WooCommerce orders `created_via 'nura_pos'`, so WooCommerce reduces stock; void = order cancelled, WooCommerce restores stock. Product tiles already expose `stock` and `in`. **POS can turn a WhatsApp order into a WC order** (sets `_nura_wa_order` on the order and `_nwo_wc_order` on the WhatsApp post, around line 470-490) - the WC order then reduces stock itself, so a WhatsApp reservation must be released at that moment to avoid a double deduction.
- **WhatsApp orders:** CPT `nurax_wa_order` (`class-nura-wa-order.php`, `class-nura-desk-orders.php`). Data in post meta `_nwo` (`items` = array of `id` (product or variation ID), `name`, `option`, `qty`, `price`). Status meta `_nwo_status`: `new`, `confirmed`, `delivered`, `cancelled`. Paid = `_nwo_pay` = `paid` (`NURAX_Desk_Orders::set_paid()`, also sets `_nwo_paid_at`) or `_nwo_paid` = `paystack` at creation. Hook available after save: `do_action( 'nurax_wa_order_saved', $post_id, $data )`. Status/payment changes are plain `update_post_meta` calls (hook `added_post_meta` / `updated_post_meta`).
- **Payment plans:** `NURAX_Desk_Plans::reserve()` already does `wc_update_product_stock( $prod, 1, 'decrease' )` and sets `stock_reserved = 1` on the plan row; cancel/delete returns it. So WC stock already excludes plan units -> On shelf = WC stock + reserved.
- **Sourced sales:** `NURAX_Desk_Source::stock_qty()` filters `woocommerce_order_item_quantity` to 0 for sourced lines - never count those.
- **Buying price:** `_nura_cost` meta on product/variation (`NURAX_Desk_Accounts`), copied to order lines at sale; only visible where `can_see_cost()`. Ledger category `stock` = "Stock bought" (kept out of profit).
- **Logging stock changes:** WooCommerce fires `woocommerce_product_before_set_stock` / `woocommerce_variation_before_set_stock` and `woocommerce_product_set_stock` / `woocommerce_variation_set_stock` - capture before/after there. Set the source context from the `woocommerce_order_item_quantity` filter (order + item, return qty unchanged; run after NURAX_Desk_Source).
- **PHP lint:** the sandbox has no PHP; a static PHP 8.3 CLI downloads from `https://dl.static-php.dev/static-php-cli/common/php-8.3.13-cli-linux-x86_64.tar.gz` (worked 13 Nov). Run `php -l` on every changed file.
- The live store could not be fetched from the agent tools on 13 Nov (SSL errors from the sandbox and web fetch); product IDs/colours came from `nura-experience/data/wa-catalogue.php`. Verify in wp-admin.

## 6a. What was built (plugin 1.110.0, 14 Nov 2026)

Files in this repo (same paths as the website repo; base = website `main` at e586a6c, plugin 1.109.4):
- `nura-experience/includes/class-nura-desk-stock.php` (new, `NURAX_Desk_Stock`, page `nurax-stock`): tables `{prefix}nurax_stock_moves` (history) and `{prefix}nurax_stock_res` (WhatsApp holds), DBV 1.0.0 / option `nurax_stock_db`.
  - Screens: Stock list (On shelf, Reserved split plan/WhatsApp, Available, Where, status, last change, filters, totals), Stock-take, History (latest 300), Held for orders, Opening buying prices (owner only). CSV downloads for stock and history.
  - Change form needs a reason (received, returned, found, damaged, lost, own use, returned to supplier, count down, stock-take). Move between places changes the split only.
  - Places: Desk settings "Stock places" (one per line, default "Studio"); split stored in product/variation meta `_nura_stock_loc`.
  - WhatsApp: reserve on `nurax_wa_order_saved` (decrease WC stock, hold `active`); `_nwo_pay`=paid -> `sold`; `_nwo_status`=cancelled -> stock back, `released`; `_nwo_wc_order` set by the till -> released first (WC order deducts itself). Paystack-paid orders go straight to `sold`. Only stock-managed items are held.
  - Plans: read-only, counts `stock_reserved = 1` rows. On shelf = WC stock + plan holds + active WhatsApp holds.
  - Every other WC stock change (orders, product edits) is logged via `woocommerce_*_set_stock` hooks.
  - Opening buying prices: sets `_nura_cost` on matched colours of products 364, 243, 274, 377 to the v4.1 averages (1934.88 / 1606.78 / 2488.59 / 2456.55). Unmatched lines (Bob Amanda, Empress, Wonderful Frontal, Negatron, LWF 2/30) excluded. Does not change stock numbers.
- `nura-experience/includes/class-nura-desk.php`: Stock tab in `header()`, page in `assets()` list, `stock_places` default/field/save.
- `nura-experience/includes/class-nura-staff.php`: permission `stock` (default on for shop managers), label, log area `stock`, perms form group "Stock".
- `nura-experience/nura-experience.php`: require + `new NURAX_Desk_Stock()`, version 1.110.0.

Released 14 Nov: owner installed 'nura-experience-1.110.0 costs v4.1', tested, and the 4 files went to the website repo (5f0e709) with HANDOVER/PROJECT-STATUS/README updated. Test: website checkout, till sale + void, WhatsApp order (place, mark paid, cancel, convert at till), payment plan reserve/cancel, sourced sale, stock-take, move, CSV downloads. Note: existing open WhatsApp orders placed before 1.110.0 are NOT held retroactively.

### Original Phase 1 shape (from PRD, with defaults)

New `nura-experience/includes/class-nura-desk-stock.php` (`NURAX_Desk_Stock`, page `nurax-stock`, own `DBV` + `dbDelta()`):
- Tables: `nurax_stock_moves` (time, product_id, variation_id, delta, before, after, reason, source, ref, location, user_id, note) and `nurax_stock_res` (source `wa`, ref post ID, product/variation, qty, status `active|sold|released`).
- Locations: names list in Desk Settings; per-location split stored per product/variation; WC stock stays the total; "Move stock" logs a move with total unchanged.
- Screens: stock list (product + colour rows; On shelf, Reserved, Available, status, last change; filters; totals), stock-take, adjust (reason required), receive (optional link to Accounts "Stock bought"), history + Excel/CSV export.
- WhatsApp: on `nurax_wa_order_saved` reserve (decrease WC stock, row `active`); on paid -> `sold`; on `cancelled` -> restore stock, `released`; on `_nwo_wc_order` added -> release first (WC order deducts). Only for products that manage stock; never block an order.
- Release: bump plugin to 1.110.0, update website `HANDOVER.md`, `PROJECT-STATUS.md`, README; build zip; owner installs. Test checkout, till sale + void, WhatsApp order, payment plan reserve/cancel, sourced sale (AGENTS.md rule 2).

## 6b. Live stock setup (14 Nov 2026)

Owner chose option 1: only the shelf pieces that match a website colour are tracked (variation-level Manage stock; all other products stay 'In stock' untracked). Loaded 22 of the 26: Loose Wave Frontal #364 Black 5 (colours 1 + 2), Burgundy 2, 33 4, Red Wine 2, 30 1; 4x4 Loose Wave Hair Closure #243 C199J 2 (= 99J), Black 2, C33 2; Bone Straight #274 Black 2. Not loaded: LWF 2/30 x1, Bob Amanda x2, 2x2 Negatron x1. Opening buying prices (v4.1) loaded on the matched colours; closure C199J set by hand (loader missed the label). Website test order #2361 reduced Burgundy 2->1 and was cancelled (restored to 2). Plugin now 1.110.1 (menu fix). Both gaps fixed in plugin 1.110.2 (installed and tested 14 Nov with test order #2363). Full detail: website repo HANDOVER.md session log 14 Nov 00:55.

## 6c. All 26 shelf pieces live in the Stock tab (14 Nov 2026, 01:15)

- Draft products, prices blank, stock tracked, v4.1 buying prices: Bob Amanda #2364 (Black var #2365 qty 1, 33 var #2366 qty 1, 1,839.90); 2x2 Negatron Closure #2367 (1/30 var #2368 qty 1, 700.00); Loose Wave Frontal #364 colour 2/30 var #2369 qty 1, 1,934.88, Enabled unticked (hidden). Stock tab: 13 lines, On shelf 26.
- **Stock places decision (owner):** all stock is kept at the Studio; Stock places stays just 'Studio'. 'Not placed yet' on the Stock list means Studio (split is written only when stock changes).
- Section 7 mapping items for these 4 lines are resolved (products created).

## 6d. Owner rule: never out of stock by itself (14 Nov 2026)

Stock held is samples to understand the trend; suppliers are on standby. Customers may order any quantity even when the shop holds 1-2. Plugin 1.111.0: tracked items keep selling at 0 (backorder shown as In stock), Available can go below 0 and the Stock list says 'Order from supplier'; only staff 'Stop selling' on the Stock tab shows Out of stock (reason required, logged). Setting 'Never show Out of stock by itself' (default on). Tested live with order #2371 (cancelled) and a qty-5 cart on Burgundy (2 in stock). Detail: website repo HANDOVER 14 Nov 01:40. Plugin 1.111.1 (14 Nov 01:55): shoppers see no 'N in stock' text, only price and Add to bag; a stopped item is stored as Out of stock so wp-admin and the Products stock filter agree (tested on Negatron #2368, undone).

## 6e. Vendor delivery 16 Nov 2026 (recorded 17 Nov, 02:45)

- 10 of the 17 awaiting pieces arrived (owner confirmed the vendor names): Body Wave 613 1, Black 1, Piano Dark 1 (website "Piano"); Loose Wave Frontal Burgundy 1 (vendor "99J"), colour 30 1; Bob Amanda 99J 1, 30 1 (new variations on draft #2364); Empress 1B 1, 1/33 1 (new draft product #2459, buying price 2,055.47); Wonderful Frontal Black 1 (vendor "Black Latisha"; stocked on the Latisha Dupe Frontal Black variation, buying price 1,000). Stock tab On shelf 26 -> 36.
- Still awaiting the vendor (7): Body Wave Piano Dark 1, 613 1, Black 1; Bone Straight High Fibre 613 2, Piano Dark 2.
- Accounts: PV-0035 (13 Nov, Stock bought, KSh 81,575) is the balance of the KSh 85,375 order. PV-0016 (3,100) and PV-0025 (700) were already recorded, so the order total in Accounts is exactly 85,375.
- Care products: buying prices loaded (see website repo HANDOVER 17 Nov 02:45); quantities not tracked yet.

## 7. Waiting on the owner

- Photos and real details (hair type, length, lace size, texture) for Bob Amanda #2364 and 2x2 Negatron Closure #2367, then publish them. Selling prices set 14 Nov: Bob Amanda Black/33 KSh 4,000, Negatron 1/30 KSh 1,800, LWF 2/30 KSh 3,500 (LWF 2/30 enabled and live). Alibaba photos were asked for, but no exact supplier listing was found and the house rule is real photos only.



- Names of stock locations (he will enter them in Settings) and which items are where.
- Website mapping decisions: Loose Wave Frontal Black colour 1 vs colour 2 (website has one "Black"); 4x4 closure 99J vs website "C1 99J"; Body Wave Piano Dark vs website "Piano"; colour 2/30 (no website option); new products for Bob Amanda, Empress, Wonderful Frontal, 2x2 Negatron (need selling prices and photos). Until then these lines are not loaded.
- Website stock counts are said to be correct, but the opening register (26 on shelf) has not been compared with WooCommerce quantities yet - do that before loading.

## 8. Session log

| Date (EAT) | Agent | Work | Commit |
|---|---|---|---|
| 13 Nov 2026 | Ray | README, AGENTS, PRD created | 2c4913b |
| 13 Nov 2026 | Ray | Opening stock transcribed from stock book photos; owner clarifications applied | b1eca2b, a2dd700, a74a129 |
| 13 Nov 2026 | Ray | Register v2.0 unit costs/IAS 2 valuation; build script; logo fixes v2.2 | c019147, 5521513 |
| 13 Nov 2026 | Ray | Draft WooCommerce mapping | fa52e05 |
| 13 Nov 2026 | Ray | Goods Received note; PRD owner decisions | bf6407c |
| 13 Nov 2026 | Ray | v3.0: only the 26 delivered pieces on shelf; 17 awaiting; 43 book total; CSV/md updated | c5cffd4, 3679da1 |
| 13 Nov 2026 | Ray | v3.1 Dashboard with charts | 44d3fa6 |
| 13 Nov 2026 | Ray | HANDOVER.md for the next agent; README/PRD refreshed | 594afa3 |
| 14 Nov 2026 | Ray | v4.0: actual making costs per product line, weighted average cost per piece; CSV, md, HANDOVER updated | 6c9ae35 |
| 14 Nov 2026 | Ray | Stock tab built (plugin 1.110.0) in `nura-experience/`; not yet released | d9512bf |
| 14 Nov 2026 | Ray | v4.1: KES 200 materials transport added (total 85,375); CSV, md, plugin buying prices updated | 1db12a1 |
| 14 Nov 2026 | Ray | Owner confirmed extra costs stay averaged per line; costs closed | 552a95a |
| 14 Nov 2026 | Ray | 1.110.0 installed and tested by owner; released to website repo 5f0e709 | 0f80e9c |
| 14 Nov 2026 | Ray | 1.110.1 menu fix; 22 pieces tracked live, buying prices loaded, test order #2361 | 9ef86b2 |
| 14 Nov 2026 | Ray | Plugin 1.110.2 (cancel restores name the order; C199J buying price) installed and tested | 22230fc |
| 14 Nov 2026 | Ray | Draft products for the 4 unmatched pieces (stock 26 on shelf); stock places stay Studio | 21b9fbb |
| 14 Nov 2026 | Ray | Selling prices set; LWF 2/30 enabled; photos pending | 6e845e4 |
| 14 Nov 2026 | Ray | Plugin 1.111.0: never out of stock by itself; Stop selling | f01db67 |
| 14 Nov 2026 | Ray | Plugin 1.111.1: stock text hidden; stopped = Out of stock in admin and lookup | (this commit) |
