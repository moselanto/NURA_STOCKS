# AGENTS.md - working on NURA Stocks

Rules for developers and AI coding agents. NURA Stocks changes a live shop, so the website repo's rules apply here too: read [moselanto/nurabeauty.co.ke AGENTS.md](https://github.com/moselanto/nurabeauty.co.ke/blob/main/AGENTS.md) and `PROJECT-STATUS.md` first.

## Golden rules

1. **WooCommerce stock is the single source of truth.** Read and write counts only through WooCommerce (`wc_update_product_stock()`, `$product->set_stock_quantity()`, `wc_get_product()`). Never keep a second, separate count that can drift.
2. **Never break checkout, the till, WhatsApp orders, payment plans or sourced sales.** After every change test: online checkout, a till sale and a void, a WhatsApp order, a payment-plan reserve and cancel, and a sourced sale (must not change shelf stock).
3. **Every change in a count is recorded** in the movement log with who, when, why, before and after. Manual changes need a reason.
4. **Do not invent counts.** Opening stock comes only from the owner's real count (stock-take). Never guess or auto-fill quantities.
5. **Buying prices stay private** (`_nura_cost`); show them only where `NURAX_Desk_Accounts` already allows (`can_see_cost()`).
6. **Staff permissions and logging:** stock actions check `NURAX_Staff::can( '<permission>' )` and write `NURAX_Staff::log()` with a valid area.
7. **Database changes** use a `DBV` constant and `dbDelta()` in `maybe_install()`. Never drop columns that hold live data.
8. **Release the website way:** bump versions, update the website repo's `HANDOVER.md`, `PROJECT-STATUS.md` and README, commit to `main`, ship a zip, owner uploads with "Replace current with uploaded", then LiteSpeed Cache > Purge All.
9. **No secrets in code.**

## Secure coding

Same checklist as the website repo: `wp_unslash()` then sanitize; escape on output; `$wpdb->prepare()`; `current_user_can()` plus nonce (`NURAX_Desk::guard()`); exports through `NURAX_Desk::csv_cell()`; `wp_safe_redirect()`.

## Coding style

WordPress Coding Standards: tabs, Yoda conditions, `array()` syntax, one class per file named `class-nura-*.php`, module header docblock.

## Testing before release

- `php -l` on every changed PHP file (PHP 8.3), JS parse check on changed JavaScript, regenerate any `.min.js`.
- Test on the live site as the owner and as a shop manager.
