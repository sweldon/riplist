INSERT INTO `equipment` (`id`, `listing_type`, `address`, `city`, `state`, `zip`, `type`, `make`, `model`, `year`, `attachments`, `hauling_options`, `trailer`, `operator`, `fuel`, `date_available`, `expiration_date`, `date_needed`, `price`, `comments`) VALUES
(1, 'sell', '6594 Point Pleasant Rd', 'Elk Grove', 'CA', '95757', '30 Ton Rough Terrain Crane', 'Grove ', 'RT530E', '2012', '', '', 'YES', 'YES', '', '2017-01-12', '2017-05-12', '0000-00-00 00:00:00', '375.00', '');


INSERT INTO `material` (`id`, `listing_type`, `address`, `city`, `state`, `zip`, `type`, `volume`, `price`, `date_available`, `expiration_date`, `load_price`, `haul_distance`, `haul_price`, `media_dir`, `notifications`, `comments`) VALUES
(1, 'sell', '323 S Park Ave', 'Aztec', 'NM', '87410', 'Gravel', '12.00', '35.00', '2017-01-02', '2017-05-26', '25.00', '20.00', '50.00', 'C:\\Users\\Steve\\Desktop\\gravel.jpg', '', 'Test Material listing');


INSERT INTO `site` (`id`, `listing_type`, `address`, `city`, `state`, `zip`, `size`, `surface`, `fenced`, `gated`, `num_entrances`, `width_entrances`, `utilities`, `ammenities`, `date_available`, `expiration_date`, `price`, `comments`) VALUES
(1, 'sell', '135 S Public Square', 'Angola', 'IN', '46703', '1 Acre', 'dirt', 'NO', 'NO', 4, '18 sq ft', 'Electricity, Water, Sewage, Natural Gas, Internet', 'Office Trailer', '2017-01-27', '2017-05-25', '1250.00', '');