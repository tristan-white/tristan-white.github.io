export function setTextToToday(id) {
    const today = new Date();
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    const formattedDate = today.toLocaleDateString(undefined, options);
    document.getElementById(id).textContent = formattedDate;
}

// calculate $ total of perks since start date
export function platTotal(open_date, close_date, intro_bonus, first) {
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

export function goldTotal(open_date, close_date, intro) {
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

export function hiltonTotal(open_date, close_date, intro_bonus) {
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

export function marriottTotal(open_date, close_date, intro_bonus) {
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

export function chaseReserveTotal(open_date, close_date, intro_bonus) {
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