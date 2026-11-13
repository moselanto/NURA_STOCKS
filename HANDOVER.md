# HANDOVER - NURA Stocks (read this first)

Last updated: 13 Nov 2026, 20:40 EAT, by Town assistant (Ray). Next agent: read this file, then `PRD.md`, then `AGENTS.md`, then the website repo's `AGENTS.md`, `PROJECT-STATUS.md` and `HANDOVER.md` ([moselanto/nurabeauty.co.ke](https://github.com/moselanto/nurabeauty.co.ke)).

## 1. What this project is

Stock control for NURA Beauty (https://nurabeauty.co.ke): a **Stock** tab inside NURA Desk (the back office in the website's `nura-experience` plugin). Code is developed in this repo under the same paths as the website repo (`nura-experience/includes/...`) and copied into the website repo for each plugin release (one plugin zip; owner installs via Plugins > Upload > "Replace current with uploaded", then LiteSpeed Cache > Purge All).

Website live versions at hand-over: theme 1.134.0, plugin `nura-experience` 1.109.3.

## 2. Status at a glance

| Item | Status |
|---|---|
| Plan (`PRD.md`) and rules (`AGENTS.md`) | Done, owner decisions recorded |
| Opening stock count (13 Nov 2026) | Done, confirmed by owner |
| Opening stock register XLSX | Done, **v3.1** (`data/`) |
| Opening stock CSV + notes | Done, match v3.1 |
| Stock lines -> website products mapping | Draft (`data/opening-stock-woocommerce-map.md`), 6 lines unmatched |
| **NURA Desk Stock tab (code)** | **Not started. Owner said "use defaults, start building" on 13 Nov.** This is the next job. |

## 3. Stock figures (source of truth: `data/opening-stock-2026-11-13.csv`)

| | Pieces | Value at cost (KES) |
|---|---|---|
| On the shelf (delivery received 13 Nov) | **26** | **53,400** |
| Awaiting the vendor | **17** | 37,850 |
| Total in the owner's stock book | **43** | 91,250 |

- Only the 26 pieces delivered on 13 Nov are on the shelf (owner, 13 Nov). Nothing else is in stock.
- Stock book quantities = what was ordered from the vendor. Ordered total 42; Loose Wave Frontal colour 33 was ordered 3 and received 4 (1 over-delivered), so the book total is 43.
- Awaiting vendor (17): Body Wave 6 (Piano Dark 2, 613 2, Black 2); Bone Straight High Fibre 4 (613 2, Piano Dark 2); Loose Wave Frontal 2 (Burgundy 1, colour 30 1); Bob Amanda 2 (99J 1, 30 1); Empress 2 (1B 1, 1/33 1); Wonderful Frontal 1 (Black).
- Delivery list wording: the 4x4 closure "burgundy x 2" = the stock book's "99J x 2" (treated as the same 2 pieces).
- Unit costs (KES per piece, owner, 13 Nov): Loose Wave Frontal 2,300; Loose Wave 4x4 Closure 1,700; Bone Straight High Fibre 2,550; Body Wave 2,450; Bob Amanda 1,300; Empress 2,000; Wonderful Frontal 1,750; 2x2 Negatron 1,000. These are also the values to enter as the website "Buying price" (`_nura_cost`).
- SKU format: `NURA-<line>-<colour>` (e.g. `NURA-LWF-33`); `/` in a colour code becomes `-`.

## 4. Files in this repo

| Path | What |
|---|---|
| `README.md` | Overview and what already exists in the website |
| `PRD.md` | Plan, phases, owner decisions |
| `AGENTS.md` | Rules for agents/developers |
| `HANDOVER.md` | This file |
| `data/NURA-Beauty-Opening-Stock-Register-2026-11-13.xlsx` | Register v3.1: Summary, Dashboard (pie, doughnut, bar, stacked column), Stock Register, Goods Received, Supplier Variances, Notes |
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

### Suggested Phase 1 shape (from PRD, with defaults)

New `nura-experience/includes/class-nura-desk-stock.php` (`NURAX_Desk_Stock`, page `nurax-stock`, own `DBV` + `dbDelta()`):
- Tables: `nurax_stock_moves` (time, product_id, variation_id, delta, before, after, reason, source, ref, location, user_id, note) and `nurax_stock_res` (source `wa`, ref post ID, product/variation, qty, status `active|sold|released`).
- Locations: names list in Desk Settings; per-location split stored per product/variation; WC stock stays the total; "Move stock" logs a move with total unchanged.
- Screens: stock list (product + colour rows; On shelf, Reserved, Available, status, last change; filters; totals), stock-take, adjust (reason required), receive (optional link to Accounts "Stock bought"), history + Excel/CSV export.
- WhatsApp: on `nurax_wa_order_saved` reserve (decrease WC stock, row `active`); on paid -> `sold`; on `cancelled` -> restore stock, `released`; on `_nwo_wc_order` added -> release first (WC order deducts). Only for products that manage stock; never block an order.
- Release: bump plugin to 1.110.0, update website `HANDOVER.md`, `PROJECT-STATUS.md`, README; build zip; owner installs. Test checkout, till sale + void, WhatsApp order, payment plan reserve/cancel, sourced sale (AGENTS.md rule 2).

## 7. Waiting on the owner

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
| 13 Nov 2026 | Ray | HANDOVER.md for the next agent; README/PRD refreshed | (this commit) |
