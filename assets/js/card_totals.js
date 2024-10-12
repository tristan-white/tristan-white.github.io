function setTextToToday(id) {
    const today = new Date();
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    const formattedDate = today.toLocaleDateString(undefined, options);
    document.getElementById(id).textContent = formattedDate;
}

// calculate $ total of perks since start date
function platTotal(open_date, close_date, intro_bonus, first) {
    const start = new Date(open_date.year, open_date.month);
    let end;
    if (close_date === undefined) {
        end = new Date();
    } else {
        end = new Date(close_date.year, close_date.month);
    }

    // calculate deltas between start and now, inclusive
    const year_delta = end.getFullYear() - start.getFullYear() + 1;
    const month_delta = (end.getFullYear() - start.getFullYear()) * 12 + (end.getMonth() - start.getMonth());

    const hotelCredit = 200 * year_delta;
    // uber credit = 15 per month + 20 in december
    const uber = (15 * month_delta) + (year_delta * 20);
    const airline = 200 * year_delta;
    // rough estimate; doesn't consider edge cases
    const saksFifthAve = 100 * year_delta;

    // I save about $30/visit to airport lounges, going about 12x per year
    const lounge = 30 * month_delta; 
    let total = hotelCredit + uber + airline + saksFifthAve + intro_bonus;
    // if this platinum is the first platinum card opened, include lounge in total
    if (first === true) total += lounge;

    const annual_fees = 695 + (Math.floor(month_delta / 12) + 1);
    
    return {
        intro: intro_bonus,
        uber: uber,
        hotel: hotelCredit,
        airline: airline,
        lounge: lounge,
        saks: saksFifthAve,
        total: total,
        annual_fees: annual_fees
    }
}

function goldTotal(open_date, close_date, intro) {
    const start = new Date(open_date.year, open_date.month);
    let end;
    if (close_date === undefined) {
        end = new Date();
    } else {
        end = new Date(close_date.year, close_date.month);
    }

    const year_delta = end.getFullYear() - start.getFullYear() + 1;
    const month_delta = (end.getFullYear() - start.getFullYear()) * 12 + (end.getMonth() - start.getMonth());

    const uber = 10 * month_delta;
    const grubhub = 10 * month_delta;
    
    // starting AUG 2024, Resy and Dunkin perks were added to card
    const new_perks = new Date(2024, 8);
    const resy = 100 * (end.getFullYear() - new_perks.getFullYear() + 1);
    const dunkin = 7 * (12 - new_perks.getMonth()) + end.getMonth() + 1;

    const annual_fees = 325 + (Math.floor(month_delta / 12) + 1);

    const total = uber + grubhub + resy + dunkin + intro;

    return {
        intro: intro,
        uber: uber,
        grubhub: grubhub,
        resy: resy,
        dunkin: dunkin,
        total: total,
        annual_fees: annual_fees, 
    }
}

function hiltonTotal(open_date, close_date, intro_bonus) {
    const start = new Date(open_date.year, open_date.month);
    let end;
    if (close_date === undefined) {
        end = new Date();
    } else {
        end = new Date(close_date.year, close_date.month);
    }
    // calculate deltas between start and now, inclusive
    const year_delta = end.getFullYear() - start.getFullYear() + 1;
    const month_delta = (end.getFullYear() - start.getFullYear()) * 12 + (end.getMonth() - start.getMonth());
    // free night at any hilton each 12 months, starting @ date of opening card
    const hotelCredit = 200 * (Math.floor(month_delta / 12) + 1);
    // $50 every quarter
    const airline = 50 * (Math.floor(month_delta / 3) + 1);
    const total = airline + hotelCredit;
    const annual_fees = 550 + (Math.floor(month_delta / 12) + 1);
    return {
        hotel: hotelCredit,
        airline: airline,
        total: total,
        annual_fees: annual_fees
    }
}

function marriottTotal(open_date, close_date, intro_bonus) {
    const start = new Date(open_date.year, open_date.month);
    let end;
    if (close_date === undefined) {
        end = new Date();
    } else {
        end = new Date(close_date.year, close_date.month);
    }
    // calculate deltas between start and now, inclusive
    const year_delta = end.getFullYear() - start.getFullYear() + 1;
    const month_delta = (end.getFullYear() - start.getFullYear()) * 12 + (end.getMonth() - start.getMonth());

    const hotelCredit = 200 * (Math.floor(month_delta / 12) + 1);
    const dining = 25 * month_delta;
    const total = dining + hotelCredit;
    const annual_fees = 650 + (Math.floor(month_delta / 12) + 1);
    return {
        dining: dining,
        hotel: hotelCredit,
        total: total,
        annual_fees: annual_fees
    }
}

function chaseReserveTotal(open_date, close_date, intro_bonus) {
    const start = new Date(open_date.year, open_date.month);
    let end;
    if (close_date === undefined) {
        end = new Date();
    } else {
        end = new Date(close_date.year, close_date.month);
    }
    // calculate deltas between start and now, inclusive
    const year_delta = end.getFullYear() - start.getFullYear() + 1;
    const month_delta = (end.getFullYear() - start.getFullYear()) * 12 + (end.getMonth() - start.getMonth());

    // estimate of amt saved on drinks/food by using a lounge * frequency
    const lounge = 30 * Math.floor(month_delta / 4); 
    const travelCredit = 300 * year_delta;
    const total = intro_bonus + travelCredit;
    const annual_fees = 550 + (Math.floor(month_delta / 12) + 1);
    return {
        travel: travelCredit,
        lounge: lounge,
        total: total,
        annual_fees: annual_fees
    }
}

setTextToToday("today1");
setTextToToday("today2");
setTextToToday("today3");

let start = {year: 2022, month: 5}; // month is zero indexed
let end = {year: 2024, month: 5}; // month is zero indexed
const gold1 = goldTotal(start, end, 800);
document.getElementById("gold1_intro").textContent = gold1.intro;
document.getElementById("gold1_uber").textContent = gold1.uber; 
document.getElementById("gold1_grubhub").textContent = gold1.grubhub;
document.getElementById("gold1_total").textContent = gold1.total;

start = {year: 2022, month: 8}; // month is zero indexed
const plat1 = platTotal(start, undefined, 1200, true);
document.getElementById("plat1_intro").textContent = plat1.intro;
document.getElementById("plat1_uber").textContent = plat1.uber; 
document.getElementById("plat1_airline").textContent = plat1.airline;
document.getElementById("plat1_hotel").textContent = plat1.hotel;
document.getElementById("plat1_saks").textContent = plat1.saks;
document.getElementById("plat1_lounge").textContent = plat1.lounge;
document.getElementById("plat1_total").textContent = plat1.total;

start = {year: 2024, month: 1}; // month is zero indexed
const plat2 = platTotal(start, undefined, 250, false);
document.getElementById("plat2_intro").textContent = plat2.intro;
document.getElementById("plat2_uber").textContent = plat2.uber; 
document.getElementById("plat2_airline").textContent = plat2.airline;
document.getElementById("plat2_hotel").textContent = plat2.hotel;
document.getElementById("plat2_saks").textContent = plat2.saks;
document.getElementById("plat2_total").textContent = plat2.total;

start = {year: 2024, month: 5}; // month is zero indexed
const plat3 = platTotal(start, undefined, 500, false);
document.getElementById("plat3_intro").textContent = plat3.intro;
document.getElementById("plat3_uber").textContent = plat3.uber; 
document.getElementById("plat3_airline").textContent = plat3.airline;
document.getElementById("plat3_hotel").textContent = plat3.hotel;
document.getElementById("plat3_saks").textContent = plat3.saks;
document.getElementById("plat3_total").textContent = plat3.total;

start = {year: 2024, month: 6}; // month is zero indexed
const gold2 = goldTotal(start, undefined, 0);
document.getElementById("gold2_uber").textContent = gold2.uber; 
document.getElementById("gold2_grubhub").textContent = gold2.grubhub;
document.getElementById("gold2_resy").textContent = gold2.resy;
document.getElementById("gold2_dunkin").textContent = gold2.dunkin;
document.getElementById("gold2_total").textContent = gold2.total;

start = {year: 2024, month: 7}; // month is zero indexed
const hilton = hiltonTotal(start, undefined, 0);
document.getElementById("hilton_airline").textContent = hilton.airline;
document.getElementById("hilton_hotel").textContent = hilton.hotel;
document.getElementById("hilton_total").textContent = hilton.total;

start = {year: 2024, month: 8}; // month is zero indexed
const marriott = marriottTotal(start, undefined, 0);
document.getElementById("marriott_dining").textContent = marriott.dining;
document.getElementById("marriott_hotel").textContent = marriott.hotel;
document.getElementById("marriott_total").textContent = marriott.total;

start = {year: 2024, month: 0} // month is zero indexed
const chase_reserve = chaseReserveTotal(start, undefined, 900);
document.getElementById("chase_reserve_travel").textContent = chase_reserve.travel;
document.getElementById("chase_reserve_lounge").textContent = chase_reserve.lounge;
document.getElementById("chase_reserve_total").textContent = chase_reserve.total;

const grand_total = plat1.total + plat2.total + plat3.total + gold1.total + gold2.total + hilton.total + marriott.total + chase_reserve.total;

document.getElementById("grand-total").textContent = `Grand Total: $${grand_total}`;
document.getElementById("saved-money").textContent = `$${grand_total}`;

const annual_fees = plat1.annual_fees + plat2.annual_fees + plat3.annual_fees + gold1.annual_fees + gold2.annual_fees + hilton.annual_fees + marriott.annual_fees + chase_reserve.annual_fees;
document.getElementById("annual-fees").textContent = `$${annual_fees}`;