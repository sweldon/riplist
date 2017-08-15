INSERT INTO `equipment` (`id`, `listing_type`, `address`, `city`, `state`, `zip`, `type`, `make`, `model`, `year`, `attachments`, `hauling_options`, `trailer`, `operator`, `fuel`, `date_available`, `expiration_date`, `date_needed`, `price`, `comments`, `images`) VALUES
(1, 'sell', '6594 Point Pleasant Rd', 'Elk Grove', 'CA', '95757', '30 Ton Rough Terrain Crane', 'Grove ', 'RT530E', '2012', '', '', 'YES', 'YES', '', '2017-01-12', '2017-05-12', '0000-00-00 00:00:00', '375.00', '', 'equipment/tcrane.jpg');


INSERT INTO `material` (`id`, `listing_type`, `address`, `city`, `state`, `zip`, `type`, `volume`, `price`, `date_available`, `expiration_date`, `load_price`, `haul_distance`, `haul_price`, `media_dir`, `notifications`, `comments`, `images`) VALUES
(1, 'sell', '323 S Park Ave', 'Aztec', 'NM', '87410', 'Gravel', '12.00', '35.00', '2017-01-02', '2017-05-26', '25.00', '20.00', '50.00', 'C:\\Users\\Steve\\Desktop\\gravel.jpg', '', 'Test Material listing', 'materials/412bd000-f915-46d8-a17f-1a52180c92f0.png,materials/89d092cc-bf43-41e3-af4a-a0a6ab325d82.PNG,materials/208551b2-d78c-4c8d-a981-dcad2ac342cb.JPG');


INSERT INTO `site` (`id`, `listing_type`, `address`, `city`, `state`, `zip`, `size`, `surface`, `fenced`, `gated`, `num_entrances`, `width_entrances`, `utilities`, `ammenities`, `date_available`, `expiration_date`, `price`, `comments`, `images`) VALUES
(1, 'sell', '135 S Public Square', 'Angola', 'IN', '46703', '1 Acre', 'dirt', 'NO', 'NO', 4, '18 sq ft', 'Electricity, Water, Sewage, Natural Gas, Internet', 'Office Trailer', '2017-01-27', '2017-05-25', '1250.00', '', 'sites/dirt.jpg');