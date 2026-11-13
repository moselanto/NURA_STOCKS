# NURA Stocks

Stock control for **NURA Beauty** (https://nurabeauty.co.ke): live stock counts for every product and every colour/length option, built as a **Stock** tab inside NURA Desk (the back office in the `nura-experience` plugin).

Status: **planning** (13 Nov 2026). No code yet. The plan is in [PRD.md](PRD.md) and waits for the owner's approval.

## Related repository

The website lives in [moselanto/nurabeauty.co.ke](https://github.com/moselanto/nurabeauty.co.ke):

| Folder | What it is |
| --- | --- |
| `nura-beauty/`, `nura-beauty-child/` | Theme (child is active) |
| `nura-experience/` | Plugin: NURA Desk (point of sale, WhatsApp orders, payment plans, sourced sales, accounts/P&L), AI stylist, bookings |

Read its `PROJECT-STATUS.md`, `AGENTS.md` and `HANDOVER.md` before changing anything that touches the store. At the time of writing the live versions are theme 1.134.0 and plugin 1.109.3.

## What already exists in the website (do not rebuild)

- WooCommerce stock fields on products and variations (`manage_stock`, `_stock`, stock status). The till (`class-nura-desk-pos.php`) already shows `stock` and in/out of stock per product and variation.
- Till sales are real WooCommerce orders (`created_via 'nura_pos'`), so WooCommerce already reduces stock when they are paid; voiding a till sale cancels the order and WooCommerce puts the stock back.
- Lipa Mdogo Mdogo payment plans can reserve one unit (`NURAX_Desk_Plans::reserve()`, `wc_update_product_stock()`, `stock_reserved` column) and return it on cancel.
- Sourced sales (`class-nura-desk-source.php`) are items sold that were not on the shelf; a filter on `woocommerce_order_item_quantity` returns 0 so they never reduce shelf stock.
- Buying price per product and per variation (`_nura_cost`, `NURAX_Desk_Accounts`), copied onto each order line at the moment of sale.
- Accounts ledger category **Stock bought** (group `stock`, kept out of profit; becomes cost of sales through the buying price when sold).
- Catalogue sync (`class-nura-desk-catalogue.php`) never touches stock.

## Files in this repo

- `README.md` - this file
- `PRD.md` - what we are building, phase by phase, plus open questions for the owner
- `AGENTS.md` - rules for developers and AI agents working here
